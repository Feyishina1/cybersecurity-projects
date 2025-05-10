#!/usr/bin/env python3

import hashlib
import sys

def crack_hash(hash_to_crack, wordlist_path, hash_type='md5'):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for line in file:
                word = line.strip()
                if hash_type == 'md5':
                    hash_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hash_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hash_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print(f"[!] Unsupported hash type: {hash_type}")
                    return

                if hash_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return

        print("[-] Password not found in the wordlist.")
    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_path}' not found.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./password_cracker.py <hash> <wordlist> <hash_type>")
        print("Example: ./password_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 rockyou.txt md5")
        sys.exit(1)

    hash_input = sys.argv[1]
    wordlist_file = sys.argv[2]
    hash_algorithm = sys.argv[3].lower()

    crack_hash(hash_input, wordlist_file, hash_algorithm)
