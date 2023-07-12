# Driving Data Quality with Data Contracts

<a href="https://www.amazon.com/Driving-Data-Quality-Contracts-comprehensive/dp/1837635005/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=&utm_source=github&utm_medium=repository&utm_campaign=9781801810135"><img src="https://m.media-amazon.com/images/I/81+QpXfjD9L._SL1500_.jpg" alt="Shipping & Fee Details" height="256px" align="right"></a>

This is the code repository for [Driving Data Quality with Data Contracts](https://www.amazon.com/Driving-Data-Quality-Contracts-comprehensive/dp/1837635005/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=&utm_source=github&utm_medium=repository&utm_campaign=9781801810135), published by Packt.

**A comprehensive guide to building reliable, trusted, and effective data platforms**

## What is this book about?

This book covers the following exciting features:
Gain insights into the intricacies and shortcomings of today’s data architectures
Understand exactly how data contracts can solve prevalent data challenges
Drive a fundamental transformation of your data culture by implementing data contracts
Discover what goes into a data contract and why it’s important
Design a modern data architecture that leverages the power of data contracts
Explore sample implementations to get practical knowledge of using data contracts
Embrace best practices for the successful deployment of data contracts

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1837635005) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter08.

The code will look like the following:
```
import pulumi 
from pulumi_gcp import bigquery 
      
default_dataset = bigquery.Dataset(  
   "defaultDataset", 
    dataset_id="pulumi_introduction", 
    friendly_name="Pulumi Introduction", 
    description="This is an example description", 
) 
```

**Following is what you need for this book:**
If you’re a data engineer, data leader, architect, or practitioner thinking about your data architecture and looking to design one that enables your organization to get the most value from your data, this book is for you. Additionally, staff engineers, product managers, and software engineering leaders and executives will also find valuable insights.

With the following software and hardware list you can run all code files present in the book (Chapter 08).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 8 | Python 3.9.12 | Windows, macOS, or Linux |
| 8 | Docker | Windows, macOS, or Linux |
| 8 | Google Cloud Platform | Windows, macOS, or Linux |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it]().

### Related products
* Data Modeling with Snowflake [[Packt]](https://www.packtpub.com/product/data-modeling-with-snowflake/9781837634453?utm_source=github&utm_medium=repository&utm_campaign=9781837634453) [[Amazon]](https://www.amazon.com/dp/1837634459)

* Data Literacy in Practice  [[Packt]](https://www.packtpub.com/product/data-literacy-in-practice/9781803246758?utm_source=github&utm_medium=repository&utm_campaign=9781803246758) [[Amazon]](https://www.amazon.com/dp/1803246758)

## Get to Know the Author
**Andrew Jones**
is a principal engineer at GoCardless, one of Europe’s leading Fintech's. He has over 15 years experience in the industry, with the first half primarily as a software engineer, before he moved into the data infrastructure and data engineering space. Joining GoCardless as its first data engineer, he led his team to build their data platform from scratch. After initially following a typical data architecture and getting frustrated with facing the same old challenges he’d faced for years, he started thinking there must be a better way, which led to him coining and defining the ideas around data contracts. Andrew is a regular speaker and writer, and he is passionate about helping organizations get maximum value from data.





