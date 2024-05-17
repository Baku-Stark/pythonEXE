import re

class RegexSys:
    @classmethod
    def model_cpf(self, cpf : str) -> str:
        cpf_model = ""

        if len(cpf) == 11:
            for index in range(0, len(cpf)):
                # print(f"{index} - {cpf[index]}")
                if index == 3 or index == 6:
                    cpf_model += f".{cpf[index]}"

                elif index == 9:
                    cpf_model += f"-{cpf[index]}"

                else:
                    cpf_model += cpf[index]

        return cpf_model

    @classmethod
    def match_cpf(self, cpf : str) -> bool:
        """
            Seguir modelo: 123.456.789-89

            args:
                cpf - String

            return:
                boolean
        """

        cpf_regex = re.compile(r"^([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})$")

        return True if re.match(cpf_regex, cpf) else False
