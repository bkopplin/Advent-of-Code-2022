let txtInput = document.getElementById('txtInput')
let btnCompute = document.getElementById('btnCompute')
let spanResult = document.getElementById('spanResult')
let spanCalories = document.getElementById('spanCalories')
let spanTotalTop3 = document.getElementById('spanTotalTop3')

btnCompute.addEventListener("click", () => {
	let i = 0
  let calPerElf = [0]
  let biggestIndex = 0
  let biggestCal = 0
  
  // for each line
  let calories = txtInput.value.split('\n')
  calories.push("")
	calories.forEach((c) => {
  	// if there's a new line, this means that we're done with the current elf
  	if (c === "") {
    	// Check if the elf's total calories are bigger than all other calories
      if (calPerElf[i] > biggestCal) {
    	biggestCal = calPerElf[i]
    	biggestIndex = i
      }
      i++
      calPerElf[i] = 0
    } else {
  		calPerElf[i] += parseInt(c)
    }
  })

  // Note that counting starts with one
  spanResult.innerHTML = biggestIndex+1
  spanCalories.innerHTML = biggestCal
  calPerElf.sort((a,b) => {return b-a})
  spanTotalTop3.innerHTML = calPerElf[0] + calPerElf[1] + calPerElf[2]

})