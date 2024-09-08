# Neo4j-to-Mssql: Migrating Data from Neo4j to Microsoft SQL Server with Django

This project provides a Python-based solution for integrating data from a Neo4j graph database to a Microsoft SQL Server database, integrated seamlessly with a Django framework. This project simplifies and streamlines the process of transferring data between these two popular database systems, making it easier for developers to manage their data across different environments.

## Features

* **Django Integration:**  The project leverages Django's robust framework, enabling you to integrate the migration process into your existing Django application.
* **Node and Relationship Mapping:**  The project maps Neo4j nodes and relationships to corresponding SQL Server tables through Django models. This allows for flexible and customizable mapping based on your specific data schema.
* **Data Conversion:**  The project handles data type conversions between Neo4j and SQL Server, ensuring data integrity during the migration process. This eliminates the need for manual data type handling.
* **Batch Processing:** The project utilizes batch processing to optimize performance and efficiently handle large datasets, making migration faster and more scalable.
* **Logging and Error Handling:** The migration process includes detailed logging capabilities to track progress and identify potential issues. Robust error handling is implemented to catch and manage unexpected exceptions, making the process more reliable.

## Getting Started

1. **Prerequisites:**
   * Python 3.x
   * Django (install with `pip install Django`)
   * Neo4j Python Driver (install with `pip install neo4j`)
   * `pyodbc` library (install with `pip install pyodbc`)
   * Microsoft SQL Server with ODBC Driver installed

