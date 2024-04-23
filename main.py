import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import csv

stopword_path = "/home/chilltoast/Desktop/Intern Assignment/StopWords/final_stopwords_list.txt"
path = "/home/chilltoast/Desktop/Intern Assignment/Extracted_Text"
file_names = ['blackassign0001', 'blackassign0002', 'blackassign0003', 'blackassign0004', 'blackassign0005',
              'blackassign0006', 'blackassign0007', 'blackassign0008', 'blackassign0009', 'blackassign0010',
              'blackassign0011', 'blackassign0012', 'blackassign0013', 'blackassign0014', 'blackassign0015',
              'blackassign0016', 'blackassign0017', 'blackassign0018', 'blackassign0019', 'blackassign0020',
              'blackassign0021', 'blackassign0022', 'blackassign0023', 'blackassign0024', 'blackassign0025',
              'blackassign0026', 'blackassign0027', 'blackassign0028', 'blackassign0029', 'blackassign0030',
              'blackassign0031', 'blackassign0032', 'blackassign0033', 'blackassign0034', 'blackassign0035',
              'blackassign0038', 'blackassign0039', 'blackassign0040', 'blackassign0041', 'blackassign0042',
              'blackassign0043', 'blackassign0044', 'blackassign0045', 'blackassign0046', 'blackassign0047',
              'blackassign0048', 'blackassign0050', 'blackassign0051', 'blackassign0052', 'blackassign0053',
              'blackassign0054', 'blackassign0055', 'blackassign0056', 'blackassign0057', 'blackassign0058',
              'blackassign0059', 'blackassign0060', 'blackassign0061', 'blackassign0062', 'blackassign0063',
              'blackassign0064', 'blackassign0065', 'blackassign0066', 'blackassign0067', 'blackassign0068',
              'blackassign0069', 'blackassign0070', 'blackassign0071', 'blackassign0072', 'blackassign0073',
              'blackassign0074', 'blackassign0075', 'blackassign0076', 'blackassign0077', 'blackassign0078',
              'blackassign0079', 'blackassign0080', 'blackassign0081', 'blackassign0082', 'blackassign0083',
              'blackassign0084', 'blackassign0085', 'blackassign0086', 'blackassign0087', 'blackassign0088',
              'blackassign0089', 'blackassign0090', 'blackassign0091', 'blackassign0092', 'blackassign0093',
              'blackassign0094', 'blackassign0095', 'blackassign0096', 'blackassign0097', 'blackassign0098',
              'blackassign0099', 'blackassign0100']
stop_words = stopwords.words("EnglishAssign")
posWords = stopwords.words("PositiveWords")
sp_sym = stopwords.words("Special_Symbols")
vowels = ["a", "e", "i", "o", "u"]
per_pro = ["I", "we", "my", "ours", "us"]
with open("/home/chilltoast/nltk_data/corpora/stopwords/NegativeWords", "r", encoding="ISO-8859-1") as txt:
    negWords = txt.readlines()
    for i in range(len(negWords)):
        if "\n" in negWords[i]:
            negWords[i] = negWords[i].removesuffix("\n")

for i in range(0, len(file_names)):
    new_text = []
    pos_list = []
    neg_list = []
    per_pro_list = []
    char_len = 0
    file_path = os.path.join(path, file_names[i])
    output_data=[]
    with open(file_path, "r") as txt:
        a = eval(str(txt.read()))
        for word in word_tokenize(a[1]):
            if word not in stop_words:  # cleaning stop words
                new_text.append(word)
                char_len += len(word)
            if word in per_pro:  # personal pronouns
                per_pro_list.append(word)
            if word in posWords:  # positive words
                pos_list.append(word)
            elif word in negWords:  # negative words
                neg_list.append(word)
        # Extracting derived variables
        positive_score = len(pos_list)
        negative_score = len(neg_list)
        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        subjectivity_score = (positive_score + negative_score) / ((len(new_text)) + 0.000001)

        # analysis of readability
        avg_sen_len = len(word_tokenize(a[1])) / len(sent_tokenize(a[1]))
        complexWords = 0
        syllable_count = 0
        for j in range(0, len(new_text)):
            vowel_count = 0
            for k in new_text[j]:
                if k in vowels:
                    vowel_count += 1
            if vowel_count > 2:
                complexWords += 1
            syllable_count = vowel_count
        fog_index = 0.4 * (avg_sen_len + (complexWords / len(new_text)))
        wps = avg_sen_len
        avg_word_len = char_len / len(new_text)
        output_data = [positive_score, negative_score, polarity_score, subjectivity_score, avg_sen_len,
                       complexWords / len(new_text), fog_index, wps, complexWords, len(new_text), syllable_count,
                       len(per_pro_list), avg_word_len]

        print(i + 1, new_text, "\n", pos_list, "\n", neg_list, "\n", "Positive Score: ",
              positive_score, "\n", "Negative Score: ", negative_score, "\n",
              "Polarity Score: ", polarity_score, "\n", "Subjectivity Score: ",
              subjectivity_score, "\n", "Average Sentence Length: ", avg_sen_len, "\n",
              "Complex Word Percentage: ", complexWords / len(new_text), "\n", "Fog Index: ", fog_index,
              "\n", "Average words per sentence: ", wps, "\n","Complex Words: ",complexWords,"\n",
              "Word Count: ",len(new_text),"\n","Syllable Count: ",syllable_count,"\n",
              "Personal Pronouns: ",len(per_pro_list),"\n","Avg Word Length: ",avg_word_len,"\n")
    with open("/home/chilltoast/Desktop/Intern Assignment/output.csv", "a",newline="") as out:
        writer = csv.writer(out, delimiter=",")
        writer.writerow(output_data)
