# Task 2: Git Bash and GitHub

## Implementation Overview
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
# Task 3: OSI Model

## Implementation Overview
In this task, I created a visual representation of the OSI model using a Draw.io diagramming tool. This diagram illustrates the seven layers of the OSI model, providing a clear overview of how data communication occurs over a network. Each layer serves a specific function and plays a crucial role in the overall data transmission process, which is essential for effective cloud computing. The diagram helps visualize the interactions between different layers, enhancing the understanding of how these layers work together to support cloud-based applications and services.

file link:- https://file.io/lQkyeCDzbZOj
## OSI Model Layers

1. **Physical Layer**:
   - Deals with the physical connection between devices, including cables, switches, and electrical signals. In cloud computing, it ensures reliable connectivity and data transmission over the internet.

2. **Data Link Layer**:
   - Responsible for node-to-node data transfer and error detection. It helps in managing how data packets are placed on the network and how they are checked for errors, crucial for maintaining data integrity in cloud environments.

3. **Network Layer**:
   - Manages the routing of data packets between devices across different networks. This layer is vital for cloud computing, as it enables communication between the cloud service provider and the client.

4. **Transport Layer**:
   - Ensures complete data transfer, managing flow control, error recovery, and data segmentation. In cloud computing, it ensures that data is delivered reliably and in the correct order.

5. **Session Layer**:
   - Establishes, maintains, and terminates communication sessions between applications. This layer is significant in cloud services for managing user sessions and maintaining connections between clients and cloud applications.

6. **Presentation Layer**:
   - Translates data between the application layer and the network format, ensuring that data is in a readable format. In cloud computing, this layer helps in data encryption and decryption, ensuring secure data exchange.

7. **Application Layer**:
   - The top layer that interfaces directly with end-user applications. It provides services for email, file transfers, and web browsing, making it essential for cloud applications to function seamlessly.

![OSI Model Diagram](https://i.imgur.com/Q6BtXks.png)

***

# Task 4: Encryption Techniques

## Implementation Overview
In this task, I implemented a basic encryption and decryption program in Python using the PyCrypto library, which introduces cryptographic algorithms. For encryption, I created a cipher using the AES algorithm in CBC mode with a 16-byte key. I padded my plaintext message to ensure it matched the required block size, then encrypted it and saved both the ciphertext and the initialization vector (IV) to a file. For decryption, I read the IV and ciphertext from the file, created a new cipher with the same key and IV, and decrypted the message. Finally, I unpadded the decrypted text to retrieve the original message. This exercise helped me understand the practical applications of encryption in securing data.

link:- https://github.com/Chandu12304/Marvel/tree/main/cryptography

![Encryption Process](https://i.imgur.com/XD7BURw.png)

***

# Task 7: Databases

## Implementation Overview
In this task, I set up a MySQL database and created a simple CRUD application using Node.js and Express.js. CRUD operations are fundamental for managing data within a database, allowing users to create, read, update, and delete records. 

link:- https://github.com/Chandu12304/MySQL--CRUD-Operation/tree/main/mysql

1. **Create**: To insert new records into a table, the SQL syntax is:
   ```sql
   INSERT INTO table_name (column1, column2) VALUES (value1, value2);
   ```

2. **Read**: To retrieve data from a table, the syntax is:
   ```sql
   SELECT * FROM table_name WHERE condition;
   ```

3. **Update**: To modify existing records, use:
   ```sql
   UPDATE table_name SET column1 = value1 WHERE condition;
   ```

4. **Delete**: To remove records from a table, the syntax is:
   ```sql
   DELETE FROM table_name WHERE condition;
   ```

Using Postman, I tested these CRUD operations by sending requests to my Express.js server, which interacted with the MySQL database to perform the respective operations. This hands-on experience enhanced my understanding of database management and querying.
![MySQL](https://i.imgur.com/t7kJK4U.png)
![MySQL](https://i.imgur.com/Qnrlkl6.png)
![MySQL](https://i.imgur.com/AcLgA6T.png)

