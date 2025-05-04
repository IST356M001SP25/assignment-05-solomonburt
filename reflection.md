# Reflection

Student Name:  Solomon Burt
Sudent Email:  sdburt@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

Completing the assignemnt 5 data pipeline reinforced the power and flexibility of the Pandas library for building ETL processes within Python. The assignment clearly demonstrated how Pandas facilitates the sequential application of data manipulation tasks, from initial data extraction and cleaning to complex transformations and the generation of analytical reports. The intuitive syntax for chaining operations, such as reading different data formats (pd.read_csv, pd.read_html), extracting information from strings (.str.extract(), .apply()), merging DataFrames (pd.merge), and creating pivot tables (pd.pivot_table), made the transformation phase feel relatively straightforward. This ease of use highlights why Pandas is a cornerstone of data analysis in Python.

However, while Pandas simplifies many data manipulation tasks, this assignment also illuminated a persistent challenge in my coding practice: optimizing for memory efficiency. I observed that my initial approaches to tasks like merging large datasets or creating new columns often resulted in code that, while functionally correct, likely consumed more memory and potentially took longer to execute than more optimized solutions. For instance, when merging the survey data with the cost of living data, I might have initially created intermediate DataFrames or used less memory-efficient join strategies before arriving at a more streamlined approach. Similarly, cleaning and transforming salary and location data could have involved creating multiple temporary columns instead of performing operations in a more memory-conscious manner.

This tendency towards less optimal memory usage stems, I believe, from a focus on achieving the desired outcome quickly, leveraging Pandas' intuitive syntax without always considering the underlying computational cost. While this allows for rapid prototyping and development, it often leads to solutions that are not scalable or efficient for larger datasets. Reviewing the professor's solutions after completing the assignment consistently reveals more elegant and memory-efficient ways to perform the same operations, often involving techniques like in-place modifications, careful data type management, or more strategic use of Pandas' indexing capabilities.

Moving forward, a key area for improvement in my learning is to proactively consider memory efficiency and performance implications during the development process, not just as a post-hoc optimization.