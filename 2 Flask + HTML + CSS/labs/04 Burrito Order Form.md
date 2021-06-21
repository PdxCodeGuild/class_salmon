

# Lab 4: Burrito Order Form


Let's create a burrito order form with the following input controls. Try to incorporate some images and semantic elements. Below are some recommended fields, feel free to use your own. You may draw some inspiration from [this image](burrito-order-form.png). 

Once you have your page together, use link at https://webhook.site/ to create a temporary endpoint. Add the attributes `action="your-url-here"` and `method="post"` to your form. Then fill out your form and submit the data. You should see an "ok" response. You can then check your bin and look at the request's body. Make sure all the relevant data is present to ensure your form is working.

- Name (text input)
- Password (password input)
- Tortilla (radio buttons)
  - White Flour
  - Wheat Flour
  - Spinach
  - Corn
- Rice (radio buttons)
  - White Rice
  - Brown Rice
- Beans (radio buttons)
  - Black Beans
  - Pinto Beans
- Protein (radio buttons)
  - Carnitas
  - Chicken
  - Sofritas
  - None
- Additional Ingredients (check boxes)
  - Cheese
  - Sour Cream
- Delivery Instructions (textarea)

## Optional

For personal info, use the `required`, `pattern` and `title` attributes of the input fields to verify that the information the user entered is legitimate.

Personal Info
- Username (at least 6 characters)
- Password (at least 6 characters)
- Name (First and Last) (two words, at lease 3 characters each)
- Email Address (one or more numbers/letters, @, one or more numbers/letters, ., one or more numbers/letters)
- Phone Number: (e.g. 293-213-5555)
- Date of Birth: (e.g. 2/13/2627)
- Social Security Number: (e.g. 415-25-2627)
- Street (e.g. 123 Mulberry Ln)
- City, State, Zip (e.g. Portland, OR, 97201)
