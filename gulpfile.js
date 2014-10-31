var gulp = require('gulp');

//var coffee = require('gulp-coffee');
var changed = require('gulp-changed');
var clean = require('gulp-clean');
var concat = require('gulp-concat');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');


var paths = {
  flash: [
    'bower_components/zeroclipboard/ZeroClipboard.swf'
  ],
  fonts: [
    'bower_components/bootstrap/fonts/*',
    'bower_components/font-awesome/fonts/*'
  ],
  images: [
    'bower_components/leaflet/dist/images/*'
  ],
  javascript: [
    //'bower_components/*/*.min.js',
    //'bower_components/*/dist/js/*min.js',
    //'bower_components/**/js/**/*.js'
  ]
};


gulp.task('clean', function () {
  return gulp.src('build', {read: false})
    .pipe(clean());
});


gulp.task('css', function () {
  return gulp.src('bower_components/**/*.min.css')
    //.pipe(sass())
    //.pipe(changed('build/assets/css/'))
    .pipe(minifycss())
    .pipe(gulp.dest('build/assets/css/'));
});


gulp.task('flash', function () {
  return gulp.src(paths.flash)
    .pipe(gulp.dest('build/assets/js/'));
});


gulp.task('fonts', function () {
  return gulp.src(paths.fonts)
    //.pipe(changed('build/assets/fonts/'))
    .pipe(gulp.dest('build/assets/fonts/'));
});


gulp.task('images', function() {
  return gulp.src(paths.images)
    //.pipe(changed('build/assets/img/'))
    .pipe(gulp.dest('build/assets/img/'));
});


gulp.task('javascript', function() {
/*
  return gulp.src(paths.javascript)
    //.pipe(coffee())
    //.pipe(changed('build/assets/js/'))
    .pipe(uglify())
    //.pipe(concat('all.min.js'))
    .pipe(gulp.dest('build/assets/js/'));
*/
});


gulp.task('plugin_css', function () {
  return gulp.src([
      'bower_components/bootstrap/dist/css/bootstrap.min.css',
      'bower_components/font-awesome/css/font-awesome.min.css',
      'bower_components/leaflet/dist/leaflet.css'
    ])
    //.pipe(changed('build/assets/css/'))
    .pipe(minifycss())
    .pipe(concat('plugins.css'))
    .pipe(gulp.dest('build/assets/css/'));
});


gulp.task('plugin_scripts', function () {
  return gulp.src([
      'bower_components/jquery/jquery.min.js',
      'bower_components/bootstrap/dist/js/bootstrap.min.js',
      'bower_components/bootstrap/js/*.js',
      'bower_components/zeroclipboard/ZeroClipboard.min.js'
    ])
    //.pipe(changed('build/assets/js/'))
    .pipe(uglify())
    .pipe(concat('plugins.js'))
    .pipe(gulp.dest('build/assets/js/'));
});


gulp.task('watch', function() {
  gulp.watch(paths.scripts, ['css', 'flash', 'fonts', 'images', 'javascript', 'plugin_css', 'plugin_scripts']);
});


gulp.task('default', ['css', 'flash', 'fonts', 'images', 'javascript', 'plugin_css', 'plugin_scripts']);
