from email_builder import EmailBuilder

def main():
    email_message = (
        EmailBuilder()
            .add_from('info@gmail.com')
            .add_to('tom@gmail.com')
            .add_to('jane@gmail.com')
            .add_cc('jim@gmail.com')
            .with_subject('The Builder Pattern Tutorial')
            .with_body('Checkout this awseoms builde pattern')
            .add_attachment('Builder Pattenn PDF')
            .build()
    )
    email_message.send()
    
    
if __name__ == '__main__':
    main()