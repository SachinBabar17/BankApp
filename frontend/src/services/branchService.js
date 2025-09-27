import axios from "axios";
const API_URL = "http://localhost:8000/branches/";

export const getBranches = async () => {
  return axios.get(API_URL);
};

export const createBranch = async (branch) => {
  return axios.post(API_URL, branch);
};