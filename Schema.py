from pydantic import BaseModel, Field
from typing import List


class Isoform(BaseModel):
    """A transcript isoform of a gene."""

    isoform_name: str = Field(description="The name of the isoform.")
    transcript_id: str = Field(description="The transcript ID of the isoform.")
    annotation_type: str = Field(description="The type of the annotation.")
    cell_types: str = Field(description="The cell type of the sample.")
    functions: List[str] = Field(description="List of functions of the transcript.")

class Gene(BaseModel):
    """A gene that has a number of transcriptome isoforms."""

    gene_name: str = Field(description="The name of the gene.")
    isoforms: List[Isoform] = Field(description="A list of transcript isoforms of the gene.")

class Article(BaseModel):
    """A scientific article containing information about genes and their isoforms."""

    article_name: str = Field(description="The name of the article.")
    authors: List[str] = Field(description="The authors of the article.")
    genes: List[Gene] = Field(description="A list of genes.")