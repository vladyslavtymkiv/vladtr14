import math

def calculate_task_estimate(a, m, b):
    E = (a + 4*m + b) / 6
    SD = (b - a) / 6
    return E, SD

def calculate_project_estimate(task_estimates):
    total_E = sum(task[0] for task in task_estimates)
    total_SD = math.sqrt(sum(task[1]**2 for task in task_estimates))
    return total_E, total_SD

def calculate_confidence_interval(project_estimate):
    E_project, SD_project = project_estimate
    CI_min = E_project - 2 * SD_project
    CI_max = E_project + 2 * SD_project
    return CI_min, CI_max

def get_user_input():
    task_estimates = []
    while True:
        a = float(input("Enter the optimistic estimate (a): "))
        m = float(input("Enter the most likely estimate (m): "))
        b = float(input("Enter the pessimistic estimate (b): "))
        task_estimates.append((a, m, b))

        choice = input("Do you want to add another task? (y/n): ")
        if choice.lower() != 'y':
            break

    return task_estimates

def print_confidence_interval(confidence_interval):
    CI_min, CI_max = confidence_interval
    print("Project's 95% confidence interval:", CI_min, "...", CI_max, "points")

if __name__ == "__main__":
    task_estimates = get_user_input()
    task_estimates = [calculate_task_estimate(a, m, b) for a, m, b in task_estimates]
    project_estimate = calculate_project_estimate(task_estimates)
    confidence_interval = calculate_confidence_interval(project_estimate)
    print_confidence_interval(confidence_interval)
