import itertools


def retornar_lista_parametro(parametros_string):
    return parametros_string.replace(",", ' ').split()


def get_dict_par():
    parametro_list = retornar_lista_parametro(input('insira os parametros como nome de variavel, '
                                                    'dividindo por ","\nEX: data_nascimento, primeiro_nome, '
                                                    'mid_nome\nNão popular as variaveis com espaço\n'
                                                    'EX: data_nascimento = 20032000 com todos os '
                                                    'caracteres: '))
    dict_var = {}
    for i in parametro_list:
        dict_var[i] = popular_var(i)
    return dict_var


def popular_var(show_in_input):
    return input(f'{show_in_input}: ')


def get_opcoes(dic_opcionais, dict_principal):
    qtd_parametro = dic_opcionais['qtd_de_parametros_usados']
    combinacoes = concatenate_dict_values(dict_principal, qtd_parametro)
    return combinacoes


def primeira_letra_maiuscula(string):
    return string.capitalize()


def full_maiusculo(string):
    return string.upper()


def concatenate_dict_values(dict_values, num_values):
    results = []
    if num_values == 2:
        combs = list(itertools.combinations(dict_values.keys(), 2))
        for key1, key2 in combs:
            value1 = dict_values[key1]
            value2 = dict_values[key2]
            value1_capt = primeira_letra_maiuscula(value1)
            value2_capt = primeira_letra_maiuscula(value2)
            value1_upper = full_maiusculo(value1)
            value2_upper = full_maiusculo(value2)
            results.append(value1 + value2)
            if not value1_capt + value2 in results:
                results.append(value1_capt + value2)
            if not value1 + value2_capt in results:
                results.append(value1 + value2_capt)
            if not value1_upper + value2 in results:
                results.append(value1_upper + value2)
            if not value1_upper + value2_capt in results:
                results.append(value1_upper + value2_capt)
            if not full_maiusculo(value1_upper + value2_upper) in results:
                results.append(value1_upper + value2_upper)
            if not value2_upper + value1 in results:
                results.append(value2_upper + value1)
            if not value2_upper + value1_capt in results:
                results.append(value2_upper + value1_capt)
            if not value2_upper + value1_upper in results:
                results.append(value2_upper + value1_upper)
            if not value2 + value1_upper in results:
                results.append(value2 + value1_upper)
            if not value2_capt + value1_upper in results:
                results.append(value2_capt + value1_upper)
            if not value2_upper + value1_upper in results:
                results.append(value2_upper + value1_upper)
            if not value1 + value2_upper in results:
                results.append(value1 + value2_upper)
            if not value1_capt + value2_upper in results:
                results.append(value1_capt + value2_upper)
            if not value1_upper + value2_upper in results:
                results.append(value1_upper + value2_upper)
            if not value2_capt + value1 in results:
                results.append(value2_capt + value1)
            if not value2 + value1_capt in results:
                results.append(value2 + value1_capt)
        return results
    if num_values == 3:
        combs = list(itertools.combinations(dict_values.keys(), 3))
        for key1, key2, key3 in combs:
            value1 = dict_values[key1]
            value2 = dict_values[key2]
            value3 = dict_values[key3]
            value1_capt = primeira_letra_maiuscula(value1)
            value2_capt = primeira_letra_maiuscula(value2)
            value3_capt = primeira_letra_maiuscula(value3)
            value1_upper = full_maiusculo(value1)
            value2_upper = full_maiusculo(value2)
            value3_upper = full_maiusculo(value3)
            results.append(value1 + value2 + value3)
            results.append(value1 + value3 + value2)
            results.append(value2 + value1 + value3)
            results.append(value2 + value3 + value1)
            results.append(value3 + value1 + value2)
            results.append(value3 + value2 + value1)
            if not value1_capt + value2 + value3 in results:
                results.append(value1_capt + value2 + value3)
            if not value1 + value2_capt + value3 in results:
                results.append(value1 + value2_capt + value3)
            if not value1 + value2 + value3_capt in results:
                results.append(value1 + value2 + value3_capt)
            if not value1_upper + value2 + value3 in results:
                results.append(value1_upper + value2 + value3)
            if not value1_upper + value2_capt + value3 in results:
                results.append(value1_upper + value2_capt + value3)
            if not value1_upper + value2 + value3_capt in results:
                results.append(value1_upper + value2 + value3_capt)
            if not value1_upper + value2_upper + value3 in results:
                results.append(value1_upper + value2_upper + value3)
            if not value1_upper + value2_upper + value3_capt in results:
                results.append(value1_upper + value2_upper + value3_capt)
            if not value1_upper + value2_capt + value3_upper in results:
                results.append(value1_upper + value2_capt + value3_upper)
            if not value1_upper + value2_capt + value3_capt in results:
                results.append(value1_upper + value2_capt + value3_capt)
            if not value2_upper + value1 + value3 in results:
                results.append(value2_upper + value1 + value3)
            if not value2_upper + value1_capt + value3 in results:
                results.append(value2_upper + value1_capt + value3)
            if not value2_upper + value1_upper + value3 in results:
                results.append(value2_upper + value1_upper + value3)
            if not value2 + value1_upper + value3 in results:
                results.append(value2 + value1_upper + value3)
            if not value2_capt + value1_upper + value3 in results:
                results.append(value2_capt + value1_upper + value3)
            if not value2 + value1_capt + value3 in results:
                results.append(value2 + value1_capt + value3)
            if not value2_capt + value1 + value3 in results:
                results.append(value2_capt + value1 + value3)
            if not value2 + value1 + value3_capt in results:
                results.append(value2 + value1 + value3_capt)
            if not value2_capt + value1_upper + value3_upper in results:
                results.append(value2_capt + value1_upper + value3_upper)
            if not value2_upper + value1_capt + value3_capt in results:
                results.append(value2_upper + value1_capt + value3_capt)
            if not value2_upper + value1_upper + value3 in results:
                results.append(value2_upper + value1_upper + value3)
            if not value2_upper + value1_upper + value3_capt in results:
                results.append(value2_upper + value1_upper + value3_capt)
            if not value2_upper + value1_capt + value3_upper in results:
                results.append(value2_upper + value1_capt + value3_upper)
            if not value2_upper + value1_upper + value3_upper in results:
                results.append(value2_upper + value1_upper + value3_upper)
            if not value2_upper + value3 + value1 in results:
                results.append(value2_upper + value3 + value1)
            if not value2_upper + value3_capt + value1 in results:
                results.append(value2_upper + value3_capt + value1)
            if not value2_upper + value3_upper + value1 in results:
                results.append(value2_upper + value3_upper + value1)
            if not value2 + value1_upper + value3_capt in results:
                results.append(value2 + value1_upper + value3_capt)
            if not value2 + value1_capt + value3_upper in results:
                results.append(value2 + value1_capt + value3_upper)
            if not value2 + value1_upper + value3_upper in results:
                results.append(value2 + value1_upper + value3_upper)
            if not value2 + value3_upper + value1_upper in results:
                results.append(value2 + value3_upper + value1_upper)
            if not value2_capt + value1_upper + value3 in results:
                results.append(value2_capt + value1_upper + value3)
            if not value2_capt + value1_upper + value3_capt in results:
                results.append(value2_capt + value1_upper + value3_capt)
            if not value2_capt + value1_capt + value3_upper in results:
                results.append(value2_capt + value1_capt + value3_upper)
            if not value2_capt + value1_capt + value3_capt in results:
                results.append(value2_capt + value1_capt + value3_capt)
            if not value2_capt + value1_capt + value3 in results:
                results.append(value2_capt + value1_capt + value3)
            if not value2_capt + value3 + value1_upper in results:
                results.append(value2_capt + value3 + value1_upper)
            if not value2_capt + value3_upper + value1 in results:
                results.append(value2_capt + value3_upper + value1)
            if not value2_capt + value3_upper + value1_upper in results:
                results.append(value2_capt + value3_upper + value1_upper)
            if not value2 + value1_upper + value3 in results:
                results.append(value2 + value1_upper + value3)
            if not value2 + value1_upper + value3_capt in results:
                results.append(value2 + value1_upper + value3_capt)
            if not value2 + value1_capt + value3_upper in results:
                results.append(value2 + value1_capt + value3_upper)
            if not value2_capt + value1 + value3_upper in results:
                results.append(value2_capt + value1 + value3_upper)
            if not value2_capt + value1_upper + value3_upper in results:
                results.append(value2_capt + value1_upper + value3_upper)
            if not value2_upper + value1 + value3_capt in results:
                results.append(value2_upper + value1 + value3_capt)
            if not value2_upper + value1_capt + value3 in results:
                results.append(value2_upper + value1_capt + value3)
            if not value2_upper + value1_capt + value3_capt in results:
                results.append(value2_upper + value1_capt + value3_capt)
            if not value2_upper + value1_upper + value3 in results:
                results.append(value2_upper + value1_upper + value3)
            if not value2_upper + value1_upper + value3_capt in results:
                results.append(value2_upper + value1_upper + value3_capt)
            if not value3 + value1 + value2 in results:
                results.append(value3 + value1 + value2)
            if not value3_capt + value1 + value2 in results:
                results.append(value3_capt + value1 + value2)
            if not value3_upper + value1 + value2 in results:
                results.append(value3_upper + value1 + value2)
            if not value3 + value1_capt + value2 in results:
                results.append(value3 + value1_capt + value2)
            if not value3_capt + value1_capt + value2 in results:
                results.append(value3_capt + value1_capt + value2)
            if not value3_upper + value1_capt + value2 in results:
                results.append(value3_upper + value1_capt + value2)
            if not value3 + value1_upper + value2 in results:
                results.append(value3 + value1_upper + value2)
            if not value3_capt + value1_upper + value2 in results:
                results.append(value3_capt + value1_upper + value2)
            if not value3_upper + value1_upper + value2 in results:
                results.append(value3_upper + value1_upper + value2)
            if not value3 + value2 + value1_upper in results:
                results.append(value3 + value2 + value1_upper)
            if not value3_capt + value2 + value1_upper in results:
                results.append(value3_capt + value2 + value1_upper)
            if not value3_upper + value2 + value1_upper in results:
                results.append(value3_upper + value2 + value1_upper)
            if not value3 + value2_capt + value1_upper in results:
                results.append(value3 + value2_capt + value1_upper)
            if not value3_capt + value2_capt + value1_upper in results:
                results.append(value3_capt + value2_capt + value1_upper)
            if not value3_capt + value1 + value2_upper in results:
                results.append(value3_capt + value1 + value2_upper)
            if not value3_capt + value1_upper + value2_upper in results:
                results.append(value3_capt + value1_upper + value2_upper)
            if not value3_capt + value2_upper + value1_upper in results:
                results.append(value3_capt + value2_upper + value1_upper)
            if not value3_upper + value1 + value2 in results:
                results.append(value3_upper + value1 + value2)
            if not value3_upper + value1_capt + value2 in results:
                results.append(value3_upper + value1_capt + value2)
            if not value3_upper + value1 + value2_capt in results:
                results.append(value3_upper + value1 + value2_capt)
            if not value3_upper + value1_capt + value2_capt in results:
                results.append(value3_upper + value1_capt + value2_capt)
            if not value3_upper + value2 + value1 in results:
                results.append(value3_upper + value2 + value1)
            if not value3_upper + value2_capt + value1 in results:
                results.append(value3_upper + value2_capt + value1)
            if not value3_upper + value2 + value1_capt in results:
                results.append(value3_upper + value2 + value1_capt)
            if not value3_upper + value2_capt + value1_capt in results:
                results.append(value3_upper + value2_capt + value1_capt)
        return results
    else:
        results = []
        for i, key in enumerate(dict_values.keys()):
            sub_dict_values = \
                {key_var: value for indice, (key_var, value) in enumerate(dict_values.items()) if indice > i}
            sub_results = concatenate_dict_values(sub_dict_values, num_values - 1)
            for sub_result in sub_results:
                value1 = dict_values[key]
                value2 = sub_result
                var_1_capt = primeira_letra_maiuscula(value1)
                var_2_capt = primeira_letra_maiuscula(value2)
                var_1_full = full_maiusculo(value1)
                var_2_full = full_maiusculo(value2)
                if not value1 + value2 in results:
                    results.append(value1 + value2)
                if not value2 + value1 in results:
                    results.append(value2 + value1)
                if not var_1_capt + value2 in results:
                    results.append(var_1_capt + value2)
                if not value2 + var_1_capt in results:
                    results.append(value2 + var_1_capt)
                if not var_1_full + value2 in results:
                    results.append(var_1_full + value2)
                if not var_2_full + value1 in results:
                    results.append(var_2_full + value1)
                if not var_1_full + var_2_capt in results:
                    results.append(var_1_full + var_2_capt)
                if not var_2_full + var_1_capt in results:
                    results.append(var_2_full + var_1_capt)
                if not var_1_full + var_2_full in results:
                    results.append(var_1_full + var_2_full)
                if not var_2_full + var_1_full in results:
                    results.append(var_2_full + var_1_full)
        return results


def rodar(return_list=True):
    dict_parametros_opcionais = {
        "qtd_de_parametros_usados": int(input('Quantidade de parametros usados (int): '))
    }
    parametros_dict = get_dict_par()
    if return_list:
        return get_opcoes(dict_parametros_opcionais, parametros_dict)
    if not return_list:
        saida = ''
        for i in get_opcoes(dict_parametros_opcionais, parametros_dict):
            saida += i + '\n'
        return saida
