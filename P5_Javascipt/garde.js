

const handleClickViewMore = (element) => {
    if(element.classList.contains("opened")){
      element.classList.remove("opened")
    }else{
      element.classList.add("opened")
    }
  }
  
  