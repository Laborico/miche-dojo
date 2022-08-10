const extractIds = require('./extract_ids_from_data_set');

describe("Extract Ids from data set", () => {
    it("No items", () => {
        const  data1 = {
            id : 1, id : 2,
            id : 3, id : 10
        }

        const data2 = {
            randomKey : 1, randomKey2 : 2,
        }

        const data3 = { }

        expect(extractIds(data1)).toBe([1, 2, 3, 10])
        expect(extractIds(data2)).toBe([])
        expect(extractIds(data3)).toBe([])
    })

    it("With items", () => {
        const  data1 = {
            id : 1, 
            id : 2,
            id : 3, 
            items : [{
                id : 4, 
                id : 5
                },{
                    id : 6
                },{
                    id : 7
                }
            ]
        }

        const data2 = {
            id : 1,
            items : [{
              id : 2,
              items : [{
                  id : 3,
                  items : [
                  {id : 4},
                  {id : 5}
                  ]
                },{
                  id : 6,
                  items : [{id : 7}]
                }]
              }]
        }

        expect(extractIds(data1)).toBe([1, 2, 3, 4, 5, 6, 7])
        expect(extractIds(data2)).toBe([1, 2, 3, 4, 5, 6, 7])
    })
})