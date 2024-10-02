# Task 2: Git Bash and GitHub

In this task, I set up a Git repository using Git Bash to manage version control. Initially, I created a new file, added text to it, and then committed and pushed the changes to the remote repository on GitHub. To further explore branching and collaboration, I created another file in a new branch, made modifications, and then created a pull request to merge my changes into the main branch. This exercise reinforced my understanding of collaborative coding practices and the importance of version control in software development.

link:- https://github.com/Chandu12304/gitBashPractice

### Git Commands Used

   ```bash
   git init
   echo "new file using master branch" > file2.txt
   git add file2.txt
   git commit -m "changes in main branch"
   git push origin main
   git checkout -b branch01
   echo "Hello" > file1.txt
   git add file1.txt
   git commit -m "message added using branch01"
   git push origin branch01
   ```
 **Create a pull request on GitHub:**
   - This is done through the GitHub web interface by navigating to the repository, switching to the new branch, and clicking on "Compare & pull request."

***
# Task 4: Encryption Techniques

## Implementation Overview
In this task, I implemented a basic encryption and decryption program in Python using the PyCrypto library, which introduces cryptographic algorithms. For encryption, I created a cipher using the AES algorithm in CBC mode with a 16-byte key. I padded my plaintext message to ensure it matched the required block size, then encrypted it and saved both the ciphertext and the initialization vector (IV) to a file. For decryption, I read the IV and ciphertext from the file, created a new cipher with the same key and IV, and decrypted the message. Finally, I unpadded the decrypted text to retrieve the original message. This exercise helped me understand the practical applications of encryption in securing data.

link:- https://github.com/Chandu12304/Marvel/tree/main/cryptography

![Encryption Process](https://i.imgur.com/XD7BURw.png)



