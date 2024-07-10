import sys
from .crew import RecruitmentCrew


def run(inputs: dict):
    """
      This function accepts a inputs in the form of a dictionary containing the 'job_requirements' and returns the output of the crew.    
    """
    try:  
      output = RecruitmentCrew().crew().kickoff(inputs=inputs)
      return output
    except Exception as e:
      raise Exception(f"An error occurred while running the crew: {e}")


def train(inputs: dict, n_iterations: int):
    """
    This function accepts inputs in the form of a dictionary containing the 'job_requirements' and 'n_iterations', and returns the output of the crew after training.
    """
    try:
        output = RecruitmentCrew().crew().train(n_iterations=n_iterations, inputs=inputs)
        return output
    
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")