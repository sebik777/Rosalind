str = 'CGCTTCTTTACTTAAGTTGCGGCCCCCTATCCTATTGTAGTCTGTATAACCGCACTATGTTACGGTCGGAGACGTCTCGTTTTCACTATGGCAAGTACCCTGGACTCACTGTTCAGATTACTTTTGCAGATAGTGGAATGGCCAGTGAGGGTCGTAACCAAGGACGACGCAGCTTTTCGGTCTTGTCCTCGTGTACATAGTCTACGCTCTAAACGCGGCGTAATACCGATTTTTGCTTCTAACCCCGCACATACTCGTCATACAGAGTATAACCCAAACGTAATAATCAAGTTAACTGAAGGTGAGTTGCTTATATTCTGTGAACGAAGGTGCTCCGGACTCATTCGCGTTAGGTGAAGTGCGCCTTCTAGTATTTCTTCCCCTACTTGGTTGCACATCACTCAAAAGCAGATCGTTCCTGCCTCAAGCGATCCTGCAATACTCTTATCTGCAGATGGCCGAAGCCTTAAATGGAGTAACTGTTCAGTGAAAACAGGATTGTAATACCAGCGATGCTCGCGAAAATATGACGTCACAGATTTGACACGGCGTGAACTAAAATCGCATTGCGGTGAGCTCCAGCCCGGAGCCTCGATAACTAGTTGGGACACGGTGTATCTACGATGGAGGAAAAGCCGAAATAAACAGATCGTTAGGTGATGATCGTAGGGCTCTTAACGGCCTGGTATAATTTTGCCGAAAAACGATAACCGTTAGTGGTAGGAAATTATAAATTTAGTTGACTGACAATAAATGGCGTAACGAACAACTTCCTCAGGAGTAGCCCGTATCGATTCTACCAAAGTAGTTAAGAGTTTGCCTAGAGGTTACTGCTCGATGTGTACCGCGTTACTCCCGAGTATTGAGATGGACACAAGGAGACTGTGAGCCGAGCAAAGGGTCCGTAAACCTATCTCA'
dict = {'A':0, 'T':0, 'G':0, 'C':0}

print(dict)

for word in str:
	dict[word] = int(dict[word]) + 1

print(dict)
for key, value in dict.items():
	print(key)
	print(value)