text1 = "Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable. This form of analysis estimates the"
text2 = "Logistic regression is a supervised machine learning algorithm widely used for binary classification tasks, such as identifying whether an email is spam or not and diagnosing diseases by assessing the presence or absence of specific conditions based on patient test results. This approach utilizes the logistic"

text1_splited = text1.split()
text2_splited = text2.split()

common = (set(text1_splited) & set(text2_splited))
words_liste = list(common)
final_liste = []

for word in words_liste :
    if len(word) > 3:
        final_liste.append(word)

print(final_liste)