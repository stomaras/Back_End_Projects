import React, {useState} from "react";

function AppleComponent() {

    const [numberOfApples, setNumberOfApples] = useState(4)

    function AppleDisplay(numberOfApples) {
        if(numberOfApples === 0 || numberOfApples === 1){
            return `John has ${numberOfApples} apple`;
        }else if (numberOfApples > 1){
            return `John has ${numberOfApples} apples`;
        }else {
            return `John owes us ${Math.abs(numberOfApples)} apples`;
        }
    }

    function IncreaseApple() {
        setNumberOfApples(currentValue => currentValue + 1)
    }

    function DecreaseApple() {
        setNumberOfApples(currentValue => currentValue - 1)
    }

    return (
    <>
        <div>
            {AppleDisplay(numberOfApples)}
        </div>  
        <button onClick={IncreaseApple} className="add-btn">Increase</button>
        <button onClick={DecreaseApple} className="decrease-btn">Decrease</button>  
    </>
    )
}

export default AppleComponent;