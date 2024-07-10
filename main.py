import sys
from crew import RecruitmentCrew


def run():
    inputs = {
        'job_requirements': """
        job_requirement:
  title: >
    Software Engineer III, Machine Learning, Search
  description: >
    Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products need to handle information at massive scale, and extend well beyond web search. We're looking for engineers who bring fresh ideas from all areas, including information retrieval, distributed computing, large-scale system design, networking and data storage, security, artificial intelligence, natural language processing, UI design and mobile; the list goes on and is growing every day. As a software engineer, you will work on a specific project critical to Google’s needs with opportunities to switch teams and projects as you and our fast-paced business grow and evolve. We need our engineers to be versatile, display leadership qualities and be enthusiastic to take on new problems across the full-stack as we continue to push technology forward.

  responsibilities: >
    - Write product or system development code.
    - Participate in, or lead design reviews with peers and stakeholders to decide amongst available technologies.
    - Review code developed by other developers and provide feedback to ensure best practices (e.g., style guidelines, checking code in, accuracy, testability, and efficiency).
    - Contribute to existing documentation or educational content and adapt content based on product/program updates and user feedback.
    - Triage product or system issues and debug/track/resolve by analyzing the sources of issues and the impact on hardware, network, or service operations and quality.

  requirements: >
    - Bachelor’s degree or equivalent practical experience.
    - 2 years of experience with software development in one or more programming languages, or 1 year of experience with an advanced degree.
    - 2 years of experience with data structures or algorithms in either an academic or industry setting.

  preferred_qualifications: >
    - Master's degree or PhD in Computer Science or related technical field.
    - 2 years of experience with machine learning algorithms and tools (e.g., TensorFlow), artificial intelligence, deep learning and/or natural language processing.
    - Experience developing accessible technologies.

  perks_and_benefits: >
    - Competitive salary and bonuses.
    - Health, dental, and vision insurance.
    - Flexible working hours and remote work options.
    - Professional development opportunities.
        """
    }
    output = RecruitmentCrew().crew().kickoff(inputs=inputs)
    return output

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'job_requirements': """
        job_requirement:
  title: >
    Software Engineer III, Machine Learning, Search
  description: >
    Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products need to handle information at massive scale, and extend well beyond web search. We're looking for engineers who bring fresh ideas from all areas, including information retrieval, distributed computing, large-scale system design, networking and data storage, security, artificial intelligence, natural language processing, UI design and mobile; the list goes on and is growing every day. As a software engineer, you will work on a specific project critical to Google’s needs with opportunities to switch teams and projects as you and our fast-paced business grow and evolve. We need our engineers to be versatile, display leadership qualities and be enthusiastic to take on new problems across the full-stack as we continue to push technology forward.

  responsibilities: >
    - Write product or system development code.
    - Participate in, or lead design reviews with peers and stakeholders to decide amongst available technologies.
    - Review code developed by other developers and provide feedback to ensure best practices (e.g., style guidelines, checking code in, accuracy, testability, and efficiency).
    - Contribute to existing documentation or educational content and adapt content based on product/program updates and user feedback.
    - Triage product or system issues and debug/track/resolve by analyzing the sources of issues and the impact on hardware, network, or service operations and quality.

  requirements: >
    - Bachelor’s degree or equivalent practical experience.
    - 2 years of experience with software development in one or more programming languages, or 1 year of experience with an advanced degree.
    - 2 years of experience with data structures or algorithms in either an academic or industry setting.

  preferred_qualifications: >
    - Master's degree or PhD in Computer Science or related technical field.
    - 2 years of experience with machine learning algorithms and tools (e.g., TensorFlow), artificial intelligence, deep learning and/or natural language processing.
    - Experience developing accessible technologies.

  perks_and_benefits: >
    - Competitive salary and bonuses.
    - Health, dental, and vision insurance.
    - Flexible working hours and remote work options.
    - Professional development opportunities.
        """
    }
    try:
        RecruitmentCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

if __name__ == "__main__":
  run()