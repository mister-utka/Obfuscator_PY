import os
import re
import random
import string

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from pprint import pprint

# путь до проекта
path_project = "./test"
# директории, которые нужно игнорировать
dirs_ignore = [".git"]

# если в переменную попадут данные значения, они будут игнорироваться
special_cases_searching_variables = ["main", "__name__", "__main__",
                                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                                     "str", "'r'", "'w'", "'a'", "'rb'", "'wb'", "'ab'", '"r"', '"w"', '"a"', '"rb"', '"rw"', '"ra"']

# если строка, которая попала под замену будет содержать одну из этих переменных, она будет игнорироваться
special_cases_substitution_variables = ["import", "from", "except", "main"]


class Obfuscator():

    # рекурсивное получение всех файлов по указанному пути
    def get_all_files_recursively(self, path):
        # создание пустого списка для хранения всех найденных файлов
        all_files = []
        # использование os.walk() для рекурсивного обхода директорий
        for root, dirs, files in os.walk(path):
            for file in files:
                # создание полного пути к файлу с использованием os.path.join()
                full_path = os.path.join(root, file)
                # игнорируем указанные директории
                if not any(ignore in full_path for ignore in dirs_ignore):
                    all_files.append(full_path)
        return all_files


    # удаление пуcтых строк и коментариев из файла
    def clearing_blank_lines_and_comments(self, path):
        try:
            with open(path, 'r') as file:
                content = file.readlines() 

            filtered_lines = [line for line in content if line.strip() and not line.strip().startswith("#")]  
            filtered_lines = [line for line in filtered_lines if line.strip() and not line.strip().startswith("print")]  

            with open(path, 'w') as n_file:
                n_file.writelines(filtered_lines)
        # если попадается бинарный файл
        except UnicodeDecodeError:
            pass


    def readlines_file(self, path):
        with open(path, 'r') as file:
            return file.readlines() 


    # поиск и сбор переменных из файлов
    def searching_variables(self, path, re_patterns):
        variables = []
        try:
            content = self.readlines_file(path)
            for line in content: 
                for re_pattern in re_patterns:
                    vars = re.findall(re_pattern, line)
                    if vars:
                        for var in vars:
                            # игнорируем все переменные, которые совпали с переменными из special_cases_searching_variables
                            if all(case != var for case in special_cases_searching_variables):
                                # если переменная не является типом данных
                                variables.append(var)
        # если попадается бинарный файл
        except UnicodeDecodeError:
            pass
        return variables


    def generating_random_string(self):
        # https://ru.stackoverflow.com/questions/1197413/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%80%D0%B0%D0%BD%D0%B4%D0%BE%D0%BC%D0%BD%D0%BE%D0%B9-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8
        text = [random.choice(string.ascii_lowercase if i != 5 else string.ascii_uppercase) for i in range(random.randint(10, 20))]
        return (''.join(text))


    def name_generation(self, list, dict):
        for name in list:
            dict[name] = self.generating_random_string()
    

    # замена всех найденных переменных
    def substitution_variables(self, path, dict):
        try:
            content = self.readlines_file(path)
            with open(path, 'w') as file:
                for line in content:
                    for key, data in dict.items():
                        if key in line:
                            if all(case not in line for case in special_cases_substitution_variables):
                                line = line.replace(key, data)
                    file.write(line)        
        except UnicodeDecodeError:
            pass


    # шифрование данных
    def encrypt_data(self, plaintext, key):
        # Create an AES cipher object with the key and AES.MODE_ECB mode
        # Создайте объект шифрования AES с ключом и режимом AES.MODE_ECB
        cipher = AES.new(key, AES.MODE_ECB)
        # Pad the plaintext and encrypt it
        # Дополните открытый текст и зашифруйте его
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        return ciphertext


    # дешифрование данных
    def decrypt_data(self, ciphertext, key):
        # Create an AES cipher object with the key and AES.MODE_ECB mode
        # Создайте объект шифрования AES с ключом и режимом BASS.MODE_ECB
        cipher = AES.new(key, AES.MODE_ECB)
        # Decrypt the ciphertext and remove the padding
        # Расшифруйте зашифрованный текст и удалите отступы
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_data


    # поиск строковых значений переменных
    def crypting_string_values(self, string_values, encryption_key):
        crypt_string_values = {}
        for s in string_values:
            s = s.replace("'","").replace('"','')
            crypt_s = self.encrypt_data(s.encode(), encryption_key)
            crypt_string_values[s] = crypt_s
        return crypt_string_values
    

    def adding_decryption_function(self, path, encryption_key):

        content = self.readlines_file(path) 

        with open(path, 'w') as file:

            key_decrypt = self.generating_random_string()
            decrypt_data = self.generating_random_string()
            cipher_crypt = self.generating_random_string()
            decrypted_data = self.generating_random_string()
            cipher_text = self.generating_random_string()
            key_crypt = self.generating_random_string()

            # Записываем новую строку
            func = f"""
{key_decrypt} = {encryption_key}
def {decrypt_data}({cipher_text}, {key_crypt}):
    {cipher_crypt} = AES.new({key_crypt}, AES.MODE_ECB)
    {decrypted_data} = unpad({cipher_crypt}.decrypt({cipher_text}), AES.block_size)
    return {decrypted_data}\n"""
            file.write(func)
            
            # Записываем остальное содержимое файла
            for line in content:
                file.write(line)
        return key_decrypt, decrypt_data


    def count_leading_spaces(self, s):
        spaces = 0
        while s.startswith(' ') and s:
            s = s[1:]
            spaces += 1
        return spaces


    # замена строковых переменных на шифрованные
    def substitution_variables_crypt(self, path, dict, key_decrypt, decrypt_data):
        try:
            content = self.readlines_file(path)
            
            with open(path, 'w') as file:
                for line in content:
                    for key, data in dict.items():
                        if key in line:
                            if all(case not in line for case in special_cases_substitution_variables):
                                line = line.replace(key, str(data))
                                re_patterns = [
                                    r"(\w*) =",
                                    r'= (".*"):',
                                    r"= ('.*'):"
                                ]
                                for re_pattern in re_patterns:
                                    var = re.findall(re_pattern, line)
                                    spaces_count = self.count_leading_spaces(line)
                                    if var:
                                        line = line.replace(line, f"{' ' * spaces_count}{var[0]} = {decrypt_data}({data}, {key_decrypt}).decode()\n")
                    file.write(line)
                        
        except UnicodeDecodeError:
            pass
    
    
    # замена кода после = на шифрованный
    def substitution_code_after(self, path, dict, key_decrypt, decrypt_data):
        command = self.generating_random_string()
        try:
            content = self.readlines_file(path)
            
            with open(path, 'w') as file:
                for line in content:
                    for key, data in dict.items():
                        if key in line:
                            if all(case not in line for case in special_cases_substitution_variables):
                                re_pattern = rf'= (.*)'
                                var = re.findall(re_pattern, line)
                                if var:
                                    
                                    spaces_count = self.count_leading_spaces(line)
                                    try:
                                        if "if" in line or "elif" in line:
                                            line = line.replace(line, f"{' ' * spaces_count}{line.split()[0]} {line.split()[1]} {line.split()[2]} {line.split()[3]}\n")
                                        else:
                                            line = line.replace(line, f"{' ' * spaces_count}{command} = {data}\n" + 
                                                                    f"{' ' * spaces_count}{command} = {decrypt_data}({command}, {key_decrypt})\n" +
                                                                    f"{' ' * spaces_count}{line.split()[0]} = eval({command})\n")
                                    except:
                                        pass
                    file.write(line)
                        
        except UnicodeDecodeError:
            pass


class Withdrawal():

    def print_inference(self, stage, code_status):
        if stage == 1:
            if code_status == 1:
                print("="*100)
                print("[*] STAGE 1: Getting all the project files")
            elif code_status == 2:
                print("[+] STAGE 1: Is completed")
                self.getting_data_from_user()
        elif stage == 2:
            if code_status == 1:
                print("="*100)
                print("[*] STAGE 2: Removing comments and blank lines from files")
            elif code_status == 2:
                print("[+] STAGE 2: Is completed")
                self.getting_data_from_user()
        elif stage == 3:
            if code_status == 1:
                print("="*100)
                print("[*] STAGE 3: Get all the existing variables and functions in the project")
            elif code_status == 2:
                print("[+] STAGE 3: Is completed")
                self.getting_data_from_user()
        elif stage == 4:
            if code_status == 1:
                print("="*100)
                print("[*] STAGE 4: Generating obfuscated names")
            elif code_status == 2:
                print("[+] STAGE 4: Is completed")
                self.getting_data_from_user()
        elif stage == 5:
            if code_status == 1:
                print("="*100)
                print("[*] STAGE 5: Name substitution")
            elif code_status == 2:
                print("[+] STAGE 5: Is completed")
        elif stage == 6:
            if code_status == 1:
                print("="*100)
                print("[*] STAGE 6: Code encryption")
            elif code_status == 2:
                print("[+] STAGE 6: Is completed")

    def getting_data_from_user(self):
        while True:
            user_input = input("Do you want to continue? (yes/no): ")
            if user_input == "yes" or user_input == "y":
                break
            elif user_input == "no" or user_input == "n":
                exit()

    def print_files(self, list_files):
        for file in list_files:
            print(file)

    def print_variables(slef, file, list_variables):
        # сортируем массив
        list_variables = sorted(list_variables)
        # удаляем повторения
        list_variables = list(dict.fromkeys(list_variables))
        print("-"*100)
        print(f"File: {file}")
        for var in list_variables:
            if var:
                print(var)

    def print_obfuscated_variables(slef, dict_obfuscated_variable):
        # получаем длину самого длинного key в словаре
        first_key_len = len(max(dict_obfuscated_variable, key=len))
        for key, data in dict_obfuscated_variable.items():
            len_key = len(key)
            # выводим данные в крисивом столбцовом форматировании
            print(f"{key}" + " "*(int(first_key_len)-int(len_key)) + f" -> {data}")



def main():

    obfuscator = Obfuscator()
    withdrawal = Withdrawal()
    encryption_key = get_random_bytes(32)

    # получение всех файлов в проекте
    withdrawal.print_inference(stage=1, code_status=1)
    all_files = obfuscator.get_all_files_recursively(path_project)
    withdrawal.print_files(all_files)
    withdrawal.print_inference(stage=1, code_status=2)

    # удаляем пустые строки и коментарии из файлов
    withdrawal.print_inference(stage=2, code_status=1)
    for file in all_files:
        obfuscator.clearing_blank_lines_and_comments(file)
    withdrawal.print_inference(stage=2, code_status=2)

    # получаем все существующие переменные в проекте
    withdrawal.print_inference(stage=3, code_status=1)
    variables = []
    for file in all_files:
        re_patterns = [
            # для переменных
            rf"(\w*)\s=",
            # для функций
            rf"def (\w*)"
            ]
        vars_file = obfuscator.searching_variables(file, re_patterns)
        if vars_file:
            variables += vars_file
            withdrawal.print_variables(file, vars_file)
    # сортируем массив и удаляем повторения
    variables = list(dict.fromkeys(sorted(variables)))
    # удаляем пустые элементы
    variables = list(filter(None, variables))
    withdrawal.print_variables("All found variables and functions:", variables)
    withdrawal.print_inference(stage=3, code_status=2)
    

    withdrawal.print_inference(stage=4, code_status=1)
    # получаем словарь {name: random_name} от переданного массива
    modified_names = {}
    obfuscator.name_generation(variables, modified_names)
    withdrawal.print_obfuscated_variables(modified_names)
    # Сортируем ключи по длине
    # так как если этого не сделать, то маленькие key могут частично заменить код переменной или функции
    modified_names = dict(sorted(modified_names.items(), key=lambda x: len(x[0]), reverse=True))
    withdrawal.print_inference(stage=4, code_status=2)


    withdrawal.print_inference(stage=5, code_status=1)
    # заменяем имена переменных и функций на новые
    for file in all_files:
        print(f"replacement statrt: {file}")
        obfuscator.substitution_variables(file, modified_names)
        print(f"replacement end:    {file}")
    withdrawal.print_inference(stage=5, code_status=2)


    withdrawal.print_inference(stage=6, code_status=1)
    # шифрование кода
    for file in all_files:

        # получение строковых значений
        re_patterns = [
            # для переменных
            rf'= (".*")$',
            # для функций
            rf"= ('.*')$"
        ]
        string_values = obfuscator.searching_variables(file, re_patterns)

        # получение словарая {значение переменной : шифрованное значение}
        crypt_string_values = obfuscator.crypting_string_values(string_values, encryption_key)

        # получение кода после =
        re_patterns = [
            # для переменных
            rf'= (.*)'
        ]
        codes_after = obfuscator.searching_variables(file, re_patterns)

        # получение словарая {значение переменной : шифрованное значение}
        crypt_codes_after = obfuscator.crypting_string_values(codes_after, encryption_key)

        # добавление функции дешифрования
        key_decrypt, decrypt_data = obfuscator.adding_decryption_function(file, encryption_key)

        # замена строковых значений на шифрованные
        obfuscator.substitution_variables_crypt(file, crypt_string_values, key_decrypt, decrypt_data)

        # замена кода после =
        obfuscator.substitution_code_after(file, crypt_codes_after, key_decrypt, decrypt_data)
    withdrawal.print_inference(stage=6, code_status=2)

    
if __name__ == "__main__":
    main()