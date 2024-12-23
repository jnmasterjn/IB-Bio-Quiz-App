export default function FisherShuffle(array){
    let i = array.length-1 //the last index

    for (; i > 0;i--){ 
        const j = Math.floor(Math.random() * (i + 1));
        [array[i],array[j]] = [array[j],array[i]]
    }
    return array
}

