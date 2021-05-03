class Luhn:
    def __init__(self, card_num, sum = 0, final_numbers = []):
        self.sum = sum
        self.card_num = card_num
        self.final_numbers = final_numbers

    def valid(self):

        card_number = self.card_num.replace(" ", "")

        if len(card_number) < 2 or card_number.isdigit() == False:
            return False

        for i in range(len(card_number)):
            if ((i+1)%2 == 0):
                number = int(card_number[-(i+1)]) * 2
                number = int(number)
                if (int(number)>9):
                    number = number - 9
                self.final_numbers.append(number)
            else:
                self.final_numbers.append(int(card_number[-(i+1)]))
        self.final_numbers.reverse()

        for num in self.final_numbers:
            self.sum += num
        if(self.sum%10 == 0):
            return True
        else:
            return False
