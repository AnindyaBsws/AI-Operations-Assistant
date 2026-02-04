from tools.github_tool import GitHubTool
from tools.weather_tool import WeatherTool

class ExecutorAgent:
    def __init__(self):
        self.github = GitHubTool()
        self.weather = WeatherTool()

    def execute(self, plan: dict):
        results = []

        for step in plan["steps"]:
            action = step["action"]
            params = step["parameters"]

            if action == "github_search":
                results.append(self.github.search_repo(**params))
            elif action == "weather_check":
                results.append(self.weather.get_weather(**params))

        return results
