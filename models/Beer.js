const mongoose = require('mongoose');

const BeerSchema = mongoose.Schema({
    name: {
        type: String,
        required: true,
        default: "Not Defined"
    },
    concentration: {
        type: Number,
        required: true,
        default: 0
    },
    type: {
        type: String,
        required: true,
        default: "Not Defined"
    },
    ingredients: {
        type: String
    },
    brewer: {
        type: String,
        required: true,
        default: "Not Defined"
    },
    originCity: {
        type: String,       
    },
    originState: {
        type: String,
    },
    originCountry: {
        type: String,
    },
    startDate: {
        type: Date,
        default: Date.now
    },
    nutrition: {
        type: Map,
        of: Number,
        default: {
            calories: 0,
            protein: 0,
            carb: 0,
            fat: 0,
            cholestrol: 0,
            sodium: 0,
            sugar: 0
        }
    }

});

module.exports = mongoose.model('Beer', BeerSchema);