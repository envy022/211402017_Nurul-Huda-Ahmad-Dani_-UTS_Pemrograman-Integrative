class BMI:
    def __init__(self, weight, height):
        self.weight = weight  # Weight in pounds
        self.height = height  # Height in feet

    def BMI_Value(self):
        """
        Menghitung nilai BMI (Body Mass Index) menggunakan berat dan tinggi.
        Formula: (berat dalam pound / (tinggi dalam kaki)^2)
        """
        return (self.weight / (self.height ** 2))

    def __eq__(self, other):
        """
        Melakukan override terhadap metode equals untuk membandingkan berat dan tinggi dua objek BMI.
        """
        return self.weight == other.weight and self.height == other.height

# Example usage:
if __name__ == "__main__":
    person1 = BMI(150, 5.5)  # Berat: 150 pound, Tinggi: 5.5 kaki
    person2 = BMI(140, 5.2)  # Berat: 140 pound, Tinggi: 5.2 kaki


    print("BMI Untuk Orang pertama :", person1.BMI_Value())
    print("BMI untuk orang kedua:", person2.BMI_Value())

    if person1 == person2:
        print("Orang 1 dan Orang 2 memiliki BMI sama.")
    else:
        print("Orang 1 dan Orang 2 memiliki BMI yang berbeda .")
