import itertools


def retornar_lista_parametro(parametros_string):
    return parametros_string.replace(",", ' ').split()


def get_dict_par():
    parametros_string = input('Insira os parâmetros como nome de variável, separados por vírgula (Ex: data_nascimento, primeiro_nome, mid_nome): ')
    parametro_list = retornar_lista_parametro(parametros_string)
    return {param: popular_var(param) for param in parametro_list}


def popular_var(param):
    return input(f'Valor para {param}: ')


def get_opcoes(dic_opcionais, dict_principal):
    qtd_parametro = dic_opcionais['qtd_de_parametros_usados']
    return concatenate_dict_values(dict_principal, qtd_parametro)


def primeira_letra_maiuscula(s):
    return s.capitalize()


def full_maiusculo(s):
    return s.upper()


def generate_combinations(values, num_values):
    combs = itertools.combinations(values, num_values)
    results = set()  # Usamos set para evitar duplicações

    for comb in combs:
        results.update(generate_all_combinations(comb))
    
    return list(results)


def generate_all_combinations(comb):
    value_combinations = []
    for perm in itertools.permutations(comb):
        value_combinations.extend(generate_variants(perm))
    return value_combinations


def generate_variants(perm):
    v1, v2 = perm
    v1_capt, v2_capt = primeira_letra_maiuscula(v1), primeira_letra_maiuscula(v2)
    v1_upper, v2_upper = full_maiusculo(v1), full_maiusculo(v2)

    variants = [
        v1 + v2, v1_capt + v2, v1 + v2_capt, v1_upper + v2, v1_upper + v2_capt,
        v1_upper + v2_upper, v2 + v1, v2_capt + v1, v2_upper + v1, v2_upper + v1_capt,
        v2_upper + v1_upper, v2_capt + v1_upper, v1 + v2_upper, v1_capt + v2_upper,
        v1_upper + v2_upper
    ]
    
    return set(variants)  # Usamos set para evitar duplicações


def concatenate_dict_values(dict_values, num_values):
    if num_values < 2 or num_values > 3:
        return generate_combinations(dict_values.values(), num_values)
    return generate_combinations(dict_values.values(), num_values)


def rodar(return_list=True):
    dict_parametros_opcionais = {
        "qtd_de_parametros_usados": int(input('Quantidade de parâmetros usados (int): '))
    }
    parametros_dict = get_dict_par()
    opcoes = get_opcoes(dict_parametros_opcionais, parametros_dict)
    
    if return_list:
        return opcoes
    return "\n".join(opcoes)
