
class Verificacao():
    def verifica_cpf_valido(self, cpf):
        try:
            """
                Fórmula de verificação do CPF

            CPF = 168.995.350-09
            ------------------------------------------------
            1 * 10 = 10           #    1 * 11 = 11 <-
            6 * 9  = 54           #    6 * 10 = 60
            8 * 8  = 64           #    8 *  9 = 72
            9 * 7  = 63           #    9 *  8 = 72
            9 * 6  = 54           #    9 *  7 = 63
            5 * 5  = 25           #    5 *  6 = 30
            3 * 4  = 12           #    3 *  5 = 15
            5 * 3  = 15           #    5 *  4 = 20
            0 * 2  = 0            #    0 *  3 = 0
                                  # -> 0 *  2 = 0
                     297          #             343
            11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
            11 > 9 = 0            #
            Digito 1 = 0          #   Digito 2 = 9
            """

            # Loop infinito
            while True:
                cpf = cpf.replace('.', '').replace('-', '')

                cpf_sem_os_dois_digitos_finais = cpf[:-2]  # Remove os dois últimos digitos do CPF
                contado_reverso = 10  # Contador reverso
                total = 0

                # Loop do CPF
                for indice in range(19):
                    if indice > 8:  # Primeiro índice vai de 0 a 9,
                        indice -= 9  # São os 9 primeiros digitos do CPF

                    total += int(cpf_sem_os_dois_digitos_finais[indice]) * contado_reverso  # Valor total da multiplicação

                    contado_reverso -= 1  # Decrementa o contador reverso
                    if contado_reverso < 2:
                        contado_reverso = 11
                        digito_do_cpf = 11 - (total % 11)

                        if digito_do_cpf > 9:  # Se o digito for > que 9 o valor é 0
                            digito_do_cpf = 0
                        total = 0  # Zera o total
                        cpf_sem_os_dois_digitos_finais += str(digito_do_cpf)  # Concatena o digito gerado no novo cpf

                # Evita sequencias. Ex.: 11111111111, 00000000000...
                sequencia = cpf_sem_os_dois_digitos_finais == str(cpf_sem_os_dois_digitos_finais[0]) * len(cpf)

                # Checando se o cpf é uma sequencia.
                if cpf == cpf_sem_os_dois_digitos_finais and not sequencia:
                    return True
                else:
                    return False
                    
        except Exception as ex:
            print(ex)