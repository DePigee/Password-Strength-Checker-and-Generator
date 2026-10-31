from collections.abc import Callable

class PasswordChecker:
    def __init__(self, rules_list: list[tuple[str, Callable[[str], bool]]]) -> None:
        self.rules = rules_list
        

    def check(self, password: str) -> dict[str, int | list[str]]:    
       checker_dict = {"score":0, "reasons":[]}

       for rule, rule_func in self.rules:
            if (rule_func(password)):
                checker_dict["score"] +=1
            else:
                checker_dict["reasons"].append(rule)
       return checker_dict 
       
