import subprocess
from emailrep import EmailRep

def main():
    pass

def check_email_with_holehe(email):
    result = subprocess.run(['holehe', email, '--only-used'], capture_output=True, text=True)
    if result.returncode != 0:
        print("An error occurred while running holehe")
        return
    output_lines = result.stdout.split('\n')
    filtered_output = [line for line in output_lines if not line.startswith("Twitter : @palenath") 
                       and not line.startswith("Github : https://github.com/megadose/holehe")
                       and not line.startswith("For BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ")]
    print("Results from Holehe:")
    for line in filtered_output:
        print(line)
def get_email_information_with_emailrep(email):
    api = EmailRep()
    try:
        response = api.query(email)
        if response:
            print("""
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     |
        :##.       ==             .###.       `.      `.    `|
        |##:                      :###:        |        >     > Email Info
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap|
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:' """)
            print("\nResults from EmailRep.io:")
            print(f"Email: {email}")
            if 'reputation' in response:
                print(f"Reputation: {response['reputation']}")
            else:
                print("Reputation: N/A")
                
            if 'details' in response:
                print(f"Details: {response['details']}")
                if 'sources' in response['details']:
                    print(f"Sources: {response['details']['sources']}")
                else:
                    print("Sources: N/A")
                print(f"Account creation date: {response['details'].get('date_creation', 'N/A')}")
                print(f"Last seen: {response['details'].get('last_seen', 'N/A')}")
                print(f"Days since last seen: {response['details'].get('days_since_last_seen', 'N/A')}")
                print(f"Blacklist status: {response['details'].get('blacklisted', 'N/A')}")
                print(f"Malicious status: {response['details'].get('malicious_activity', 'N/A')}")
            else:
                print("Details: N/A")
        else:
            print(f"No information found for {email}")
    except Exception as e:
        print(f"Error querying EmailRep.io: {str(e)}")

if __name__ == "__main__":
    email = input("Enter the email address: ")
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)

if __name__ == "__main__":
    main()