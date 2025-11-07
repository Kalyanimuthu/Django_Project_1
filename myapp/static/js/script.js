document.addEventListener("DOMContentLoaded", function() {
  const addToCartBtn = document.querySelector('.btn-primary');
  if (addToCartBtn) {
    addToCartBtn.addEventListener('click', () => {
      alert("Product added to cart!");
    });
  }
});
