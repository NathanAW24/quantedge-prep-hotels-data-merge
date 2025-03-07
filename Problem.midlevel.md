# Hotels data merge

## Introduction

To write the application you can use any language. It should work as a web server. You can post it as a gist, upload to GitHub or send us via email, anything works as long as the code is correct, completed and you send us instructions how to use it.

## Background

In any hotels site like Kaligo.com operated by Ascenda, there's a lot of effort being made to present content in a clean & organised manner. Underneath the hood however, the data procurement process is complex and data is often mismatched & dirty.

This exercise gives you a sneak peak in some of the actions we take to clean up data before it makes it to the site

- we are querying multiple suppliers to assimilate data for these different sources
- we are building the most complete data set possible
- we are sanitizing them to remove any dirty data
- etc.

The task is to write a simplified version of our data procurement & merging process.

It needs to work in the following way:

## Requirements

1. Merge hotel data of different suppliers
2. Parse and clean dirty data
3. Select what you think is the best data to deliver using some simple rules
4. Deliver it via an API endpoint by you which allows us to query the hotels data with some simple filtering

The system input and output requirements are stated below.

### Request

- Endpoint should support the following parameters: destination, hotels
- When requested, the server should fetch the results filtered by:
  - hotels: based on a list of hotel IDs given
  - destination: based on a given destination ID
- Each hotel should be returned only once (since you've already uniquely merged the data)

### Response

1. Response should be returned in an organised format. An example is shown below.
2. If you elect to modify the response format, do specify why you think your elected choice is better.

```
[
  {
    "id": "iJhz",
    "destination_id": 5432,
    "name": "Beach Villas Singapore",
    "location": {
      "lat": 1.264751,
      "lng": 103.824006,
      "address": "8 Sentosa Gateway, Beach Villas, 098269",
      "city": "Singapore",
      "country": "Singapore"
    },
    "description": "Surrounded by tropical gardens, these upscale villas in elegant Colonial-style buildings are part of the Resorts World Sentosa complex and a 2-minute walk from the Waterfront train station. Featuring sundecks and pool, garden or sea views, the plush 1- to 3-bedroom villas offer free Wi-Fi and flat-screens, as well as free-standing baths, minibars, and tea and coffeemaking facilities. Upgraded villas add private pools, fridges and microwaves; some have wine cellars. A 4-bedroom unit offers a kitchen and a living room. There's 24-hour room and butler service. Amenities include posh restaurant, plus an outdoor pool, a hot tub, and free parking.",
    "amenities": {
      "general": ["outdoor pool", "indoor pool", "business center", "childcare", "wifi", "dry cleaning", "breakfast"],
      "room": ["aircon", "tv", "coffee machine", "kettle", "hair dryer", "iron", "bathtub"]
    },
    "images": {
      "rooms": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/3.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg", "description": "Bathroom" }
      ],
      "site": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/1.jpg", "description": "Front" }
      ],
      "amenities": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg", "description": "RWS" }
      ]
    },
    "booking_conditions": [
      "All children are welcome. One child under 12 years stays free of charge when using existing beds. One child under 2 years stays free of charge in a child's cot/crib. One child under 4 years stays free of charge when using existing beds. One older child or adult is charged SGD 82.39 per person per night in an extra bed. The maximum number of children's cots/cribs in a room is 1. There is no capacity for extra beds in the room.",
      "Pets are not allowed.",
      "WiFi is available in all areas and is free of charge.",
      "Free private parking is possible on site (reservation is not needed).",
      "Guests are required to show a photo identification and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Payment before arrival via bank transfer is required. The property will contact you after you book to provide instructions. Please note that the full amount of the reservation is due before arrival. Resorts World Sentosa will send a confirmation with detailed payment information. After full payment is taken, the property's details, including the address and where to collect keys, will be emailed to you. Bag checks will be conducted prior to entry to Adventure Cove Waterpark. === Upon check-in, guests will be provided with complimentary Sentosa Pass (monorail) to enjoy unlimited transportation between Sentosa Island and Harbour Front (VivoCity). === Prepayment for non refundable bookings will be charged by RWS Call Centre. === All guests can enjoy complimentary parking during their stay, limited to one exit from the hotel per day. === Room reservation charges will be charged upon check-in. Credit card provided upon reservation is for guarantee purpose. === For reservations made with inclusive breakfast, please note that breakfast is applicable only for number of adults paid in the room rate. Any children or additional adults are charged separately for breakfast and are to paid directly to the hotel."
    ]
  }
]
```

### Suppliers

There are 3 suppliers of hotel data, each of them has a different URL:
  - https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme
  - https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia
  - https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies

You can assume the following about the supplier data:

- IDs are clean & sanitized
  - All supplier endpoints return consistently matching hotel & destination IDs
  - You can merge them based off these IDs
- Image links from the suppliers are already verified as working, you only need to worry about the organization of image data for it
- Please note that for the simplification and ease of testing these are static URLs, they always return the same values, but you shouldn't treat them as static content (e.g. your information procurement should react dynamically over time if I decide to add or remove a hotel from 1 of the supplier datasets)

## Expectations

For this exercise, we will evaluate

1. Your decisions on data cleaning & selecting the best data; how you deal with different datatypes & nuances from supplier-provided data
2. Solution design
3. Tests (Both unit & feature tests)

For the purposes of this interview, you're dealing with a smaller dataset and a smaller range of suppliers. In production, we work with several more suppliers, and a larger scale of data.

Your design should account for this and be easy to improve & extend in the long run. For Senior Engineer (and above) candidates, you're expected to ensure the API is reasonably fast.

No data-analytics approach is needed for this exercise, we're not looking for any fancy machine-learning evaluation for merging the data, some simple rules in code for matching the data is sufficient.

### Bonuses

- Optimizations for speed and robustness in the data procurement/delivery process
- Demonstrate any 1 of the following skills
  - Deployment
  - Test pipeline

### What we don't want from you?

We can skip the overly complex build or bonus decisions; the goal of the exercise is to show your experience - we don't want you to sweat days over the solution (then that defeats the purpose of the exercise).

Examples of complicated actions we don't need you to do:
- Entire AWS account & pipeline setup (taking days) to show live deployment
- Solving for attribute selection using some ML-based approach

## Questions?

If you have any questions, don't worry, just send me an email/schedule a call, I'll respond as quickly as I can.

If needed, we can also do a quick follow-up call before you embark on the exercise.

Good luck!
