from db_config import local_session, create_all_entities
from Country import Country
from AirlineCompany import AirlineCompany
from Flight import Flight
from UserRole import UserRole
from User import User
from Administrator import Administrator
from Customer import Customer
from Ticket import Ticket


def main():
    try:
        create_all_entities()

        local_session.commit()
        # local_session.add(UserRole(role_name='Administrator'))
        # local_session.add(UserRole(role_name='Customer'))
        # local_session.add(UserRole(role_name='AirCompany'))
        #
        # local_session.commit()

    except Exception as e:
        print(f'Error! : {str(e)}')


main()

