function extractItems(list){
    let ids = []
    list.forEach(function(item){
      ids.push(...extractIds(item))
    })
    return ids
  }
  
  function extractIds(data){
    let ids = []
    for (const key in data) {
      if(key === "id"){
        ids.push(data[key])
      } else if (key === "items"){
        ids.push(...extractItems(data["items"]))
      }
    }
    return ids
  }