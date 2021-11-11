# Nesting lint in Dict
cars_company = {
    "Volvo": {
        'caars_i_like': [
            'Volvo XC90',
            'Volvo XC60',
            'Volvo XC40',
            'Volvo S90',
            'Volvo S60',
            'Volvo XC40 Recharge'
        ]
    },

    "BMW": {
        'BMW X1': 'Price ₹63.40 Lakh',
        'BMW 3 Series': 'price ₹57.89 Lakh',
        'BMW X7': 'price ₹ 1.07 Crore',
        'BMW Z4': 'price ₹ 69.77 Lakh',
        'BMW 5 Series': 'price ₹ 69.77 Lakh'
    }
}
print(cars_company)

# Nesting dict in dict
cars_volvo = {
    "Volvo": {
        'caars_i_like': [
            'Volvo XC90',
            'Volvo XC60',
            'Volvo XC40',
            'Volvo S90',
            'Volvo S60',
            'Volvo XC40 Recharge'
        ]
    }
}

# Nesting Dict in list

cars_company_all = [
    {
        "Volvo": {
            'caars_i_like': [
                'Volvo XC90',
                'Volvo XC60',
                'Volvo XC40',
                'Volvo S90',
                'Volvo S60',
                'Volvo XC40 Recharge'
            ]
        },

        "BMW": {
            'BMW X1': 'Price ₹63.40 Lakh',
            'BMW 3 Series': 'price ₹57.89 Lakh',
            'BMW X7': 'price ₹ 1.07 Crore',
            'BMW Z4': 'price ₹ 69.77 Lakh',
            'BMW 5 Series': 'price ₹ 69.77 Lakh'
        }
    }
]
