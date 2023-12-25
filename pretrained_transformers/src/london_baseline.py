# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import tqdm
import utils
file_path = '../birth_dev.tsv'  # Replace with the actual file path

# Open the file and read it line by line
with open(file_path, 'r', encoding='utf-8') as file:
    correct = 0 
    num_lines = 0
    for line in file:
        num_lines+=1
        # Process each line as needed
        #print(line.strip())  # This example prints each line without leading or trailing whitespace
        x = line.split('\t')[1].strip()
        if x == "London":
            correct+=1
print('Correct: {} out of {}: {}%'.format(correct, num_lines, correct/num_lines*100))

