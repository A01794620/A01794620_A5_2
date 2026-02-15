# Exercise of Programming 2 and Static Analysis 5.2

|                                 |                                                            |
|---------------------------------|------------------------------------------------------------|
| Author                          | Ronald Sandí Quesada                                       |
| Student-ID                      | A01794620                                                  |
| E-mail                          | A01794620@tec.mx                                           |
| MNA Class                       | Pruebas de Software y Aseguramiento de la Calidad (TC4017) |
| **Professors:**                 |                                                            |
| &nbsp;&nbsp;Professor           | PhD. Gerardo Padilla Zárate                                |
| &nbsp;&nbsp;Evaluator and Tutor | PhD. Daniel Flores Araiza                                  |
| Period                          | I Trimester 2026                                           |
| Date                            | 15/02/20226                                                |

## Introduction.

This document exhibits the dynamic of coding and applying static analysis for quality assurance 
on traditional computational problems.

The process of building a valid deliverable is described in the next main steps:

1.	Understanding the main problem and its specific requirements.
2.	Installation of the support libraries to prepare the environment, especially Pylint and Flake8.
3.	Coding the solution.
4.	Initial testing for preparing the environment.
5.	Testing using Pylint static analysis tool, under PEP-8 standards. 
6.  Fixing inconsistencies and bugs detected by Pylint. 
7.  Testing using Flake8 analysis tool, under PEP-8 standards.
8.  Fixing inconsistencies and bugs detected by Flake8.
9.  Assessing the solution by using a battery of tests prepared in advance.

## Product deliverable.

The following deliverable is the main part of the final solution.

Program for the Programming Individual Exercise: 5.2:

---
* **Program #1. Computing Sales:** this applicative takes two files:
  * One file containing a database of Products and their specs.
  * One file having the sales performed by those products.
* The motive of the program is to compile the sales totals using the information from both files.
* There is a calculation yielded from unitary price (taken from first file, and the quantity taken form the second file).
---

## Structure of the Project.

The GitHub repository has the following structure.

**Table 1.** Project structure in GitHub repository.

| Folder in A01794620_A5_2 repository | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1st. Test Case                                                                                                                                                       | 2nd. Test Case                                                                      | 3rd. Test Case                                                                        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| results                             | It is a folder where all the computation information is stored on plain files. Every result folder has the same structure: i. **Name of file:** it is the name of the original file, converting its extension to a valid file format name. ii. **Subfolder UTC:** using UTC time, one subfolder per run is created to preserve old runs, avoiding collisions. iii. **Conventional name per exercise:** for example, running a test case file name `TC1.Sales.json` in the first test, where the conventional name is `SalesResults`, it might yield an output file path like this: `results/TC1_Sales_json/1770949018_572289/SalesResults.txt` | [Go](https://github.com/A01794620/A01794620_A5_2/tree/main/results/TC1_Sales_json/)                                                                                  | [Go](https://github.com/A01794620/A01794620_A5_2/tree/main/results/TC2_Sales_json/) | [Go](https://github.com/A01794620/A01794620_A5_2/tree/main/results/TC3_Sales_json/)   |
| src                                 | It is the folder where the software solution is placed. It represents one executable Python file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Go](https://github.com/A01794620/A01794620_A5_2/tree/main/src)                                                                                                      | `idem`                                                                              | `idem`                                                                                |
| tests                               | The folder from where all the files are respectively read and used as raw material for the automatic -or manual- testing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Go](https://github.com/A01794620/A01794620_A5_2/tree/main/tests)                                                                                                    | `idem`                                                                              | `idem`                                                                                |
| common                              | Folder that holds helpers and auxiliary classes that support the solution holistically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Go](https://github.com/A01794620/A01794620_A5_2/tree/main/common)                                                                                                   | `idem`                                                                              | `idem`                                                                                |
| qa_assess                           | Batch files that automate the QA testing processes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Go](https://github.com/A01794620/A01794620_A5_2/tree/main/qa_assess)                                                                                                | `idem`                                                                              | `idem`                                                                                |

## Quality Assurance using Pylint.

The first set of documented tests are the ones done with `Pylint` tool.

The initial Run yielded inconsistencies that the investigator must debug, correct and fix.

This image displays the errors found in the first documented run.

![ss_01.png](https://github.com/A01794620/A01794620_A5_2/blob/main/pics/ss_01.png)
_Image 1. First Pylint round in the main deliverable._

The previous depiction shows the result on the program. 

> [!NOTE]
> Final run, after fixing inconsistencies and bugs: after several tweaks, the investigator can obtain the grade often pursued, Image 2 shows that moment.

![ss_02.png](https://github.com/A01794620/A01794620_A5_2/blob/main/pics/ss_02.png)
_Image 2. Pylint test passed._

The Image 2 displays the testing phase in the main solution files, nevertheless the following table summarize the Pylint debug process on each of the miscellaneous classes for the solution.

Having 10.0 grade was a back-and-forth process, a big learning on how to use test static code tools. 

Majority of the issues were related to the following problems:

1. Final new line missing.
2. Missing docstring in functions or in classes. 
3. Name of the file: by introducing the clause of disable the _C0103_ code check (the snake type of files) the issue was sorted. 
4. Lines were too long: those were easily fixed by breaking the lines.
5. In minor degree, but found, the imports conflicts with the common libraries done ad-hoc for the project (Common_Functions); here the strategy of disabling both: wrong-import-position and import-error per line scope fixed the issues.
6. Some coincidences on functions with too many arguments. Depending on the cases disabling the codes _R0913_ and _R0917_ or in others fixing the big number of parameters.

_A full copy of Pylint results can be found [here](https://github.com/A01794620/A01794620_A5_2/blob/main/results/qa_assess_reports/pylint_final_report.txt)_


## Quality Assurance using Flake8.
-- Fill here the details using Flake8

## Test Cases:

The test cases are products of too much of back-and-forth between run, fix and rerun.

Nevertheless, in the end it is possible to obtain and deliver a set of battery test cases.

The process was improved until it reached automatic batch processing.

## Positive Test Cases.

The following three images document the three positive test cases. As described on Table 1, on each specific  case 
in side the `result` folder, there is granulated fashion display in all the tests. The list as following:

* Test Case 1 report folder [Here](https://github.com/A01794620/A01794620_A5_2/tree/main/results/TC1_Sales_json/).
* Test Case 2 report folder [Here](https://github.com/A01794620/A01794620_A5_2/tree/main/results/TC2_Sales_json/)
* Test Case 3 report folder [Here](https://github.com/A01794620/A01794620_A5_2/tree/main/results/TC3_Sales_json/). 

_Image 4. Assess cases successful passed on the program._

On Image 4, the [A] side shows a properly parsed file while the [B] zone displays how the program detects few lines
with inconsistencies, but even though it keeps running until the end of the file in process.

On Image 5, there are three zones: i. Zone [A] shows the first part of a long result-set. ii. Then [B] part is the
'tail' of results, including important information like the elapsed time in run the computations plus also the one
which took on paint in screen plus saving the results at file (this second extremely more time-consuming than the former).

## Negative -Intended- Test Cases.

Inside the cases, it is possible to check, that even when wrong files path were provided, the solutions is robust,
checking the veracity of the path/file, and gracefully handling any scenario derived.

So, the solution supported in a robust fashion those obstacles.

The properly handling inconsistencies in data are displayed on next image.

<!-- ![pic_pylint_01.png](https://github.com/A01794620/A01794620_A5_2/tree/main/pics/pic_pylint_01.png) -->
_Image 7. Trying the robustness of programs using wrong files paths._

> [!IMPORTANT]
> **Addendum**: Some tips to clear.

## Methodological references.

The commits of the project had been performed using the techniques described in Buchea(2026) and 
Conventional Commits (2026).

## APA References:
* Conventional Commits (2026). Conventional Commits. Recovered on February 12, 2026 form https://www.conventionalcommits.org/en/v1.0.0/
* Buchea, J. (2026). Semantic Commit Messages. Recovered on February 12, 2026 from https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
