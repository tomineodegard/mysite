async function tweet() {
    const frm = event.target;
   
    const conn = await fetch("/tweet", {
     method: "POST",
     body: new FormData(frm),
    });
    const data = await conn.json();
    console.log(data);
    
}