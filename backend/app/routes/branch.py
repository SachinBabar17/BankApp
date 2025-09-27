from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.branch import Branch
from app.utils.schemas import Branch as BranchSchema, BranchCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BranchSchema)
def create_branch(branch: BranchCreate, db: Session = Depends(get_db)):
    db_branch = Branch(name=branch.name, address=branch.address)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

@router.get("/", response_model=list[BranchSchema])
def get_branches(db: Session = Depends(get_db)):
    return db.query(Branch).all()

@router.get("/{branch_id}", response_model=BranchSchema)
def get_branch(branch_id: int, db: Session = Depends(get_db)):
    branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch