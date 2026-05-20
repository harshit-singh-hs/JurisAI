import os
import re
import requests

def is_article_in_part(article_num, file_name):
    art = article_num.strip().upper()
    part = file_name.upper().replace(".TXT", "")
    
    match = re.match(r'^(\d+)', art)
    if not match:
        return False
    num = int(match.group(1))
    
    if part == 'PART1':
        return 1 <= num <= 4
    elif part == 'PART2':
        return 5 <= num <= 11
    elif part == 'PART3':
        return 12 <= num <= 35
    elif part == 'PART4':
        return 36 <= num <= 51 and not art.endswith('A')
    elif part == 'PART4A':
        return art == '51A'
    elif part == 'PART5':
        return 52 <= num <= 151
    elif part == 'PART6':
        return 152 <= num <= 237
    elif part == 'PART7':
        return num == 238
    elif part == 'PART8':
        return 239 <= num <= 242
    elif part == 'PART9':
        if num != 243:
            return False
        if art == '243':
            return True
        suffix = art[3:]
        return len(suffix) == 1 and 'A' <= suffix <= 'O'
    elif part == 'PART9A':
        if num != 243:
            return False
        suffix = art[3:]
        if len(suffix) == 1:
            return 'P' <= suffix <= 'Z'
        elif len(suffix) == 2:
            return suffix[0] == 'Z' and 'A' <= suffix[1] <= 'G'
        return False
    elif part == 'PART9B':
        if num != 243:
            return False
        suffix = art[3:]
        return len(suffix) == 2 and suffix[0] == 'Z' and 'H' <= suffix[1] <= 'T'
    elif part == 'PART10':
        return 244 <= num <= 244 or art == '244A'
    elif part == 'PART11':
        return 245 <= num <= 263
    elif part == 'PART12':
        return 264 <= num <= 300 or art == '300A'
    elif part == 'PART13':
        return 301 <= num <= 307
    elif part == 'PART14':
        return 308 <= num <= 323
    elif part == 'PART14A':
        return art in ('323A', '323B')
    elif part == 'PART15':
        return 324 <= num <= 329 or art == '329A'
    elif part == 'PART16':
        return 330 <= num <= 342
    elif part == 'PART17':
        return 343 <= num <= 351
    elif part == 'PART18':
        return 352 <= num <= 360
    elif part == 'PART19':
        return 361 <= num <= 367
    elif part == 'PART20':
        return num == 368
    elif part == 'PART21':
        return 369 <= num <= 392
    elif part == 'PART22':
        return 393 <= num <= 395
    return False

def fetch_and_generate_corpus():
    files = [
        'Preamble.txt', 'PART1.txt', 'PART2.txt', 'PART3.txt', 'PART4.txt', 'PART4A.txt',
        'PART5.txt', 'PART6.txt', 'PART7.txt', 'PART8.txt', 'PART9.txt', 'PART9A.txt',
        'PART9B.txt', 'PART10.txt', 'PART11.txt', 'PART12.txt', 'PART13.txt', 'PART14.txt',
        'PART14A.txt', 'PART15.txt', 'PART16.txt', 'PART17.txt', 'PART18.txt', 'PART19.txt',
        'PART20.txt', 'PART21.txt', 'PART22.txt', 'SCHEDULE1.txt', 'SCHEDULE2.txt',
        'SCHEDULE3.txt', 'SCHEDULE4.txt', 'SCHEDULE5.txt', 'SCHEDULE6.txt', 'SCHEDULE7.txt',
        'SCHEDULE8.txt', 'SCHEDULE9.txt', 'SCHEDULE10.txt', 'SCHEDULE11.txt', 'SCHEDULE12.txt'
    ]
    
    output_dir = "d:/Project/Online-Legal-Advisor/data/legal_corpus"
    os.makedirs(output_dir, exist_ok=True)
    
    # Clear existing constitution files to prevent orphans or corruption
    print("Clearing old constitution files...")
    for filename in os.listdir(output_dir):
        if filename.startswith("constitution_"):
            os.remove(os.path.join(output_dir, filename))
            
    print(f"Creating legal corpus files in: {output_dir}")
    
    full_constitution_contents = []
    file_count = 0
    
    for file_name in files:
        url = f"https://raw.githubusercontent.com/captn3m0/constitution/master/{file_name}"
        print(f"Downloading {file_name}...")
        res = requests.get(url)
        if res.status_code != 200:
            print(f"Failed to download {file_name}")
            continue
            
        content = res.text
        
        # Add to full constitution list
        full_constitution_contents.append(f"=== START OF {file_name.upper()} ===\n{content}\n=== END OF {file_name.upper()} ===")
        
        # If it's a PART file, split into individual Articles
        if file_name.startswith("PART"):
            # Articles start with a number followed by a period at the beginning of a line
            pattern = re.compile(r'\n(\d+[A-Z]?)\.\s+')
            matches = list(pattern.finditer(content))
            
            if not matches:
                # Save whole file if no article headers matched
                out_path = os.path.join(output_dir, f"constitution_{file_name.lower()}")
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(content)
                file_count += 1
                continue
                
            # Split and save each article
            for i, match in enumerate(matches):
                start = match.start()
                end = matches[i+1].start() if i + 1 < len(matches) else len(content)
                article_text = content[start:end].strip()
                article_num = match.group(1)
                
                # Check range validation
                if not is_article_in_part(article_num, file_name):
                    continue
                
                # Prepend "Article " so that searches match Article numbers exactly
                cleaned_text = f"Article {article_text}"
                
                out_path = os.path.join(output_dir, f"constitution_article_{article_num}.txt")
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(f"CONSTITUTION OF INDIA - {file_name}\n\n{cleaned_text}")
                file_count += 1
        else:
            # Preamble and Schedules are saved as complete files
            prefix = "constitution_preamble.txt" if file_name == "Preamble.txt" else f"constitution_{file_name.lower()}"
            out_path = os.path.join(output_dir, prefix)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"CONSTITUTION OF INDIA\n\n{content}")
            file_count += 1
            
    # Save the full concatenated constitution to constitution_full.txt
    full_path = os.path.join(output_dir, "constitution_full.txt")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(full_constitution_contents))
    file_count += 1
    print(f"Saved consolidated full constitution to: {full_path}")
            
    print(f"\nSuccessfully generated {file_count} files in the legal corpus directory.")

if __name__ == "__main__":
    fetch_and_generate_corpus()
