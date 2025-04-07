
        
    
        
        
        $(document).ready(function() {

          
            
             /* $('#add-item').click(function(e) {
                e.preventDefault();

                
    
                 var formsetTable = $('#formset-items');
                var lastRow = formsetTable.find('.formset-row:last');
                var newRow = lastRow.clone(true);
    
                // Clear input values in the cloned row
                newRow.find('input').val('');
    
                // Append the cloned row to the table
                formsetTable.append(newRow);  
            }); */

            $('.datepicker').datepicker({
                dateFormat: 'dd-mm-yy',  // Set the date format to match input_formats
                changeYear: true,
                changeMonth: true,
                autoclose: true
            });

           

            
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
   });

   $('#sidebarCollapse').on('click', function () {
       $('#sidebar').toggleClass('active');
       $('.collapse.in').toggleClass('in');
        // and also adjust aria-expanded attributes we use for the open/closed arrows
        // in our CSS
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
   });


   $('#id_0-brand').select2({
    selectOnClose: true
  });

  $('#id_0-category').select2({
    selectOnClose: true
  });

  $('#allocate_serial').select2({
    selectOnClose: true
  });
  /* $('#id_user').select2({
    selectOnClose: true
  }); */

  


  
  $(window).on('scroll', function() {
    var windowHeight = $(window).height();
    var scrollPos = $(window).scrollTop();
    
    $('.counter-count').each(function() {
      var offsetTop = $(this).offset().top;
      
      if (offsetTop < scrollPos + windowHeight / 2 && !$(this).hasClass('animated')) {
        $(this).addClass('animated').prop('Counter', 0).animate({
          Counter: $(this).text()
        }, {
          duration: 10000,
          easing: 'swing',
          step: function(now) {
            $(this).text(Math.ceil(now));
          }
        });
      }
    });
  });
 


  
        });
        
       