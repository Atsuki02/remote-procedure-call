// define and export requests

const floorRequest = {
    method: "floor",
    params: [42.8],
    id: 1
};


const nrootRequest = {
    method: "nroot",
    params: [2, 16],
    id: 2
};


const reverseRequest = {
    method: "reverse",
    params: ["hello"],
    id: 3
};


const validAnagramRequest = {
    method: "validAnagram",
    params: ["listen", "silent"],
    id: 4
};


const sortRequest = {
    method: "sort",
    params: [["banana", "apple", "cherry", "date"]],
    id: 5
};

module.exports = {
    floorRequest,
    nrootRequest,
    reverseRequest,
    validAnagramRequest,
    sortRequest
};