import readData
from pattern import VALIDATION_SCHEMA
import json
import pytest
from readData import basic_tool

all_data = readData.read('/Users/edward.zhang/Desktop/some.csv')
TEST_CASES = ['iban', 'swift_code', 'account_name', 'account_number', 'account_routing_type1', 'account_routing_type2',
              'account_routing_value1', 'account_routing_value2', 'state', 'postcode']


class Test_apiSchemaTest2():

    def findPattern(self, fields, target_value):
        for index, value in enumerate(fields):
            if value['key'] == target_value:
                return value['rule']['pattern']
        return ''

    def selector(self, country_code, payment_method, lcs, account_currency, entity_type):
        select_result = []
        for case in TEST_CASES:
            test_schemas = VALIDATION_SCHEMA[case]
            for index, schema in enumerate(test_schemas):
                split_schema = list(schema)[0].split('/')
                country_code_schema, payment_method_schema, lcs_schema, account_currency_schema, entity_type_schema \
                    = split_schema
                if (country_code in country_code_schema or country_code_schema == '*') and \
                        (payment_method in payment_method_schema or payment_method_schema == '*') and \
                        (lcs in lcs_schema or lcs_schema == '*') and \
                        (account_currency in account_currency_schema or account_currency_schema == '*') and \
                        (entity_type in entity_type_schema or entity_type_schema == '*'):
                    select_result.append(list(schema.values())[0]['pattern'])
                    break
                elif index == len(test_schemas) - 1:
                    select_result.append('')
        return select_result

    def get_pattern(self, data):
        entity_type, payment_method, account_currency, country_code, lcs = data[0], data[1], data[2], data[3], data[4]
        payload = {
            "entity_type": entity_type,
            "payment_method": payment_method,
            "account_currency": account_currency,
            "bank_country_code": country_code,
            "local_clearing_system": lcs}
        if not payload['local_clearing_system']:
            payload.pop('local_clearing_system')
        expect = self.selector(country_code, payment_method, lcs, account_currency, entity_type)
        r = basic_tool.sendRequest(payload)
        json_r = json.loads(r.text)
        patterns = [self.findPattern(json_r['fields'], case) for case in TEST_CASES]
        return expect, patterns

    @pytest.mark.parametrize('data', readData.read("/Users/edward.zhang/Desktop/some.csv"),
                             ids=readData.str_data(all_data))
    def test_all(self, data):
        country_code = data[3]
        expects, patterns = self.get_pattern(data)
        self.show_cases(expects)
        print('-------------------------------------------------------------------------------------')
        self.show_cases(patterns)
        for index, expect in enumerate(expects):
            if expect == '':
                if TEST_CASES[index] == 'account_name':
                    pytest.assume(('^.{2,100}$' == patterns[index]),
                                  '--------Testing {} --------'.format(TEST_CASES[index]))
                else:
                    pytest.assume('' == patterns[index], '--------Testing {} --------'.format(TEST_CASES[index]))
            else:
                if 'country' in expect:
                    expect = expect.replace('country', country_code)
                x= patterns[index]
                pytest.assume(expect == x, '--------Testing {} --------'.format(TEST_CASES[index]))

    def show_cases(self, cases):
        show_cases = []
        for index, case in enumerate(cases):
            show_cases.append(TEST_CASES[index] + " : " + case)
        print(show_cases)

if __name__ == "__main__":
    pytest.main(
        ["-v", "testApiSchema2.py::Test_apiSchemaTest2::test_all", "--html=/Users/edward.zhang/Desktop/report2.html"])
