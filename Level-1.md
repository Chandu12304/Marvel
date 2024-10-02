# Task 2: Git Bash and GitHub

In this task, I set up a Git repository using Git Bash to manage version control. Initially, I created a new file, added text to it, and then committed and pushed the changes to the remote repository on GitHub. To further explore branching and collaboration, I created another file in a new branch, made modifications, and then created a pull request to merge my changes into the main branch. This exercise reinforced my understanding of collaborative coding practices and the importance of version control in software development.

link:- https://github.com/Chandu12304/gitBashPractice

### Git Commands Used

1. **Initialize a new Git repository:**
   ```bash
   git init
   ```

2. **Create a new file and add text:**
   ```bash
   echo "new file using master branch" > file2.txt
   ```

3. **Add the file to the staging area:**
   ```bash
   git add file2.txt
   ```

4. **Commit the changes:**
   ```bash
   git commit -m "changes in main branch"
   ```

5. **Push changes to the remote repository:**
   ```bash
   git push origin main
   ```

6. **Create a new branch:**
   ```bash
   git checkout -b branch01
   ```

7. **Create another file and make changes:**
   ```bash
   echo "Hello" > file1.txt
   git add file1.txt
   git commit -m "message added using branch01"
   ```

8. **Push the new branch to the remote repository:**
   ```bash
   git push origin branch01
   ```

9. **Create a pull request on GitHub:**
   - This is done through the GitHub web interface by navigating to the repository, switching to the new branch, and clicking on "Compare & pull request."

