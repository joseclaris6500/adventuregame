'Name of title'
TITLE = 'Space Cowboys'
URGENT = '''In the distant planet of Gallafry there is a group of outlawed
 space cowboys. We need your help to find and kill the group named The Sons of the Fallen.
  So join our cause to liberaty the people of Gallafry.'''
HERO = 'Oscar Weltflower'
FIRST_PROMPT = '''Welcome traveler, thank you for answering the call to join our cause to regain our home
from those rebels. You are now standing in front of our last remain base of operations. Here are your first tasks to
be prepared for Operation White Jewel'''
FIRST_PROMPT_CHOICES = '''
1) Find the Teller
2) Go to the amory
3) Start training
4) Vencher off by yourself'''

CAMP_JACK_OPTIONS = '''
You have '''
def main():
    print(TITLE)
    print(URGENT)
    print(FIRST_PROMPT)
    task_options = input(FIRST_PROMPT_CHOICES)

if __name__ == '__main__':
    main()