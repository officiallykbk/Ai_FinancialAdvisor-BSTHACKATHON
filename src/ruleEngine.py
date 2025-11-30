def applyRules(data):
    tags=[]
    score = 0
    history = data['history']

    total_salary = sum(i['salary'] for i in history)
    total_spending = sum(i['spending'] for i in history)
    total_saving = sum(i['saving'] for i in history)

    
    avg_salary = total_salary / len(history)  

    # Track changes month-to-month
    salary_list = [i['salary'] for i in history]
    spending_list = [i['spending'] for i in history]

    # savings rate checking
    savings_rate = (total_saving / total_salary) * 100

    if savings_rate < 10:
        tags.append("Low Savings Rate")
        score -= 4
    elif savings_rate < 25:
        tags.append("Moderate Savings")
        score += 1
    else:
        tags.append("High Savings Rate")
        score += 4

    # spending trend checking
    if spending_list[-1] > spending_list[0] * 1.3:
        tags.append("Increasing Spending Trend")
        score -= 3
    elif spending_list[-1] < spending_list[0] * 0.8:
        tags.append("Improving Spending Discipline")
        score += 3

    # income stability
    salary_volatility = max(salary_list) - min(salary_list)

    if salary_volatility > avg_salary * 0.25:
        tags.append("Income Volatility")
        score -= 3
    else:
        tags.append("Stable Income")
        score += 2

    # salary vs spending
    burn_rate = (total_spending / total_salary) * 100

    if burn_rate > 80:
        tags.append("High Burn Rate")
        score -= 3
    elif burn_rate < 60:
        tags.append("Healthy Burn Rate")
        score += 3

    score = max(-10, min(10, score))
    return {"tags": tags, "score": score, "note":"Score is between -10 to 10"}
