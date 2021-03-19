##Test Case
1. UTM settings on Newsletter design page 
2. input warning message, for example, on Journey SMS page when we try to save empty title input
3.	on Journey do list filter input 
4.	'Test' radio button on smart recommender launch step 
5.	on Journey do list how to click exactly needed campaign’s Statistics button if there is more than 1 campaigns in the list
6.	on Message box design page remove variation cross icon
7.	Remove/ Change element buttons on Journey canvas page
8. Alert toaster on any page of panel
9. on Social Proof ‘Create New Personalization’

###Locators

1) $$('#enableUTMSettings_')
2) $$('#message-attribute')
3) $$('#search-value')
4) $x('//*[contains(@label,'Test')]') 
5) $$('.statistics')[0]
6) $x('//*[contains(text(),'Delete')]')
7) $x('.//*[contains(text(),'Delete')]')
8) $$('#toast')
9) $$('#create-mobile-campaign')



