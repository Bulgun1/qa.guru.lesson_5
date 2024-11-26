from selene import browser, have
import os

from selene.support.conditions.have import value


def test_demoqa_form():

    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Robert')
    browser.element('#lastName').type('Mopski')

    browser.element('#userEmail').type('Robert@gmail.com')

    browser.element('[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('7980909090')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2003"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="6"]').click()
    #browser.all('.react-datepicker__month-select>option').element_by(have.exact_text("July")).click()
    browser.element('.react-datepicker__day.react-datepicker__day--007').click()



    browser.element('#subjectsInput').type('English').press_tab()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('test.png'))
    browser.element('#currentAddress').type('г.Москва ул.Василия Ощепкова 6')

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()


    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            "Robert Mopski",
            "Robert@gmail.com",
            "Male",
            "7980909090",
            "07 July,2003",
            "English",
            "Music",
            "test.png",
            "г.Москва ул.Василия Ощепкова 6",
            "NCR Gurgaon",
        )
    )




