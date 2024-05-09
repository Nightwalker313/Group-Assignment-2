import os
from radon.complexity import cc_visit
from radon.metrics import mi_visit

def calculate_metrics(project_path):
    """Calculate CC and MI metrics for a given project path."""
    cc_results = []
    mi_results = []

    # Iterate over Python files in the project path
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    source_code = f.read()
                    cc_results.extend(cc_visit(source_code))
                    mi_results.extend(mi_visit(source_code))

    # Calculate average Cyclomatic Complexity (CC) and Maintainability Index (MI)
    total_cc = sum([cc.complexity for cc in cc_results])
    average_cc = total_cc / len(cc_results) if cc_results else 0

    total_mi = sum([mi for _, mi in mi_results])
    average_mi = total_mi / len(mi_results) if mi_results else 0

    return average_cc, average_mi

# Define the project paths
project_paths = [
    "apache-commons-lang-1.2/src/main/java",
    "apache-commons-math-3.6.1/src/main/java",
    "hadoop-common-project-2.2.0-tests/hadoop-common/src/main/java",
    "lucene-solr-8.11.0/lucene/src/java",
    "poi-bin-5.2.2-20220220/src/main/java",
    "elasticsearch-7.16.1/src/main/java",
    "gson-2.10/java-src-main",
    "jhipster-7.9.3/generators/server/src/main/resources/templates",
    "junit-4.13.2/src",
    "mockito-3.11.2/src/main/java"
]

for project_path in project_paths:
    project_path = os.path.join("C:/Users/Night/Desktop/this", project_path)
    # Calculate cyclomatic complexity and maintainability index for each project
    # Assuming you have a function to calculate these metrics
    cc, mi = calculate_metrics(project_path)
    print(f"Project: {project_path}")
    print(f"Average Cyclomatic Complexity (CC): {cc}")
    print(f"Average Maintainability Index (MI): {mi}")
    print()