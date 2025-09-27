import React, { useEffect, useState } from "react";
import { getBranches, createBranch } from "../services/branchService";

export default function BranchComponent() {
  const [branches, setBranches] = useState([]);
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");

  useEffect(() => {
    fetchBranches();
  }, []);

  const fetchBranches = async () => {
    const response = await getBranches();
    setBranches(response.data);
  };

  const addBranch = async () => {
    await createBranch({ name, address });
    setName("");
    setAddress("");
    fetchBranches();
  };

  return (
    <div>
      <h2>Branches</h2>
      <ul>
        {branches.map((branch) => (
          <li key={branch.id}>{branch.name} - {branch.address}</li>
        ))}
      </ul>
      <input placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
      <input placeholder="Address" value={address} onChange={(e) => setAddress(e.target.value)} />
      <button onClick={addBranch}>Add Branch</button>
    </div>
  );
}